from math import ceil, floor

import logging
import datetime

class dataObject(object):
	"""
	Defines a time-series style object which contains a name, dynamical function, and raw data array.

	attributes:
		name = string identifier of the object
		func = time-dependent function which is used to calculate values of object at different times.
		           Can also be a constant value which will be returned at all times.
		*args= other time-dependent functions or arguments which are to be passed to func
	"""
	def __init__(self,name,func,*args):
		logging.disable(logging.ERROR)
		self.args = args	# dependencies of this function
		self.data = list()           # time series data list
		self.name = name
		#logging.debug(str(name)+' args='+str(ar) for ar in self.args)
		if func==None:
			raise ValueError('getter function not specified for dataObject '+str(self.name))
		elif hasattr(func, '__call__'): #function is given
			logging.debug(str(name)+' getter function saved.')
			self.calc = func  # function for calculating value at given time
		else : #non-callable data given, assume constant function
			logging.debug(str(name)+' is constant valued.')
			self.calc = lambda t: func

	def __call__(self, t=None):
		if t==None:	        # if no time specified, spit out all the data we have
			return self.data

		# please don't be upset by how unpythonic this next part is... I'm going to come back and add functionality, I promise.
		elif isinstance(t, datetime.date):	# if time given is a date
			#TODO: convert it to int using deltatime & carry on 
			raise RuntimeError('call with date not yet supported')
		elif isinstance(t, datetime.datetime):
			#TODO: convert it to int using deltatime & carry on 
			raise RuntimeError('call with datetime not yet supported')
		elif isinstance(t, datetime.timedelta):
			#TODO: convert it to int using deltatime & carry on 
			raise RuntimeError('call with timedelta not yet supported')
		elif t+1 < len(self.data): # if already calculated for this time, use previous value
			return linearInterpolate(self.data,t)
		else:	              # new time, solve as initial value problem from last known point
			for i in range(len(self.data),int(ceil(t+1))):
				if len(self.args) == 0: #if no arguments
					self.data.append(self.calc(i))
				else:
					try: #use the given arguments
						self.data.append(self.calc(i,*self.args))
					except TypeError as e:#wrong number of arguments, try passing raw data array
						if e.message.split('type')[0] == 'unsupported operand ':
							raise
						else:
							logging.warn('typical usage of dataObject fails'
								         +'\n\tERR:'+e.message
								         +'\n\tARGS given: time,'+str([str(arg) for arg in self.args])
								         +'\n\traw data access granted to calculating function '+str(self.calc)+'to find @t='+str(t))
							self.calc(self.data,t,*self.args)
							break
			return linearInterpolate(self.data,t)
	logging.disable(logging.NOTSET)

	# sets a new function for calculating values given a time t and other optional arguments
	def setFunction(self,f,*args):
		self.data = list()	# clear any data so far
		self.calc = f
		self.args = args

	# clears all data and resets to default
	def reset(self):
		self = dataObject(self.name,self.func)

# linear interpolation for the PECS data object class
def linearInterpolate(data,t):
	"""
	Simple linear interpolation using the given data array
	"""
	logging.disable(logging.DEBUG)	#comment this line if debugging this function; otherwise disables to avoid log clutter

	# custom return function to handle onExit behaviors
	def prepExit( val ):
		logging.disable(logging.NOTSET)	# undo logging disable
		return val

	if t%1 < .0001 or t%1 >.9999:	#if t is really close to int
		return prepExit( data[int(t)] )
	else:
		#linearly interpolate between data points
		logging.debug('m = (y2-y1)/1 = ('+str(data[int(ceil(t))])+'-'+str(data[int(floor(t))])+')/1')
		m = data[int(ceil(t))]-data[int(floor(t))]	#slope
		x = t%1	#dist from known value
		b = data[int(floor(t))]	#known value
		logging.debug('y = mx+b = '+str(m)+'*'+str(x)+'+'+str(b))
		return prepExit( m*x + b )
