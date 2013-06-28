from math import ceil, floor

import logging
import datetime

class dataObject(object):
	def __init__(self,func=None,*args):
		self.data = list()           # time series data list

		if func==None:
			logging.warn('getter function not specified for dataObject;'+\
			             ' I will set a temporary function for now and hope you change it later.')
			self.calc = lambda t: t*0.1
		else :
			self.calc = func  # function for calculating value at given time

		self.args = args	# dependencies of this function

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
				if len(self.args) == 0:
					self.data.append(self.calc(i))
				else:
					self.data.append(self.calc(self,i,*self.args))
			return linearInterpolate(self.data,t)

	# sets a new function for calculating values given a time t and other optional arguments
	def setFunction(self,f,*args):
		self.data = list()	# clear any data so far
		self.calc = f
		self.args = args

	# clears all data and resets to default
	def reset(self):
		self = dataObject()

# linear interpolation for the PECS data object class
def linearInterpolate(data,t):
	if t%1 < .0001 or t%1 >.9999:	#if t is really close to int
		return data[int(t)]
	else:
		#linearly interpolate between data points
		logging.debug('m = (y2-y1)/1 = ('+str(data[int(ceil(t))])+'-'+str(data[int(floor(t))])+')/1')
		m = data[int(ceil(t))]-data[int(floor(t))]	#slope
		x = t%1	#dist from known value
		b = data[int(floor(t))]	#known value
		logging.debug('y = mx+b = '+str(m)+'*'+str(x)+'+'+str(b))
		return m*x + b
