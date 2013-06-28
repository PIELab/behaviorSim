from math import ceil, floor

import logging

class dataObject(object):
	def __init__(self):
		self.data = list()           # time series data list
		self.calc = lambda t,args=None: t*0.1  # function for calculating value at given time

	def __call__(self, t=None, args=None):
		if t==None:	        # if no time specified, spit out all the data we have
			return self.data
		elif t+1 < len(self.data): # if already calculated for this time, use previous value
			return linearInterpolate(self.data,t)
		else:	              # new time, solve as initial value problem from last known point
			for i in range(len(self.data),int(ceil(t+1))):
				if args == None:
					self.data.append(self.calc(i))
				else:
					self.data.append(self.calc(i,args))
			return linearInterpolate(self.data,t)

	# sets a new function for calculating values given a time t and other optional arguments
	def setFunction(self,f):
		# TODO: checks?
		self.data = list()	# clear any data so far
		self.calc = f

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
