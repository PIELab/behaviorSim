from math import ceil, floor

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
				self.data.append(self.calc(i,args))
			return linearInterpolate(self.data,t)

# linear interpolation for the PECS data object class
def linearInterpolate(data,t):
	if t%1 < .0001 or t%1 >.9999:	#if t is really close to int
		return data[int(t)]
	else:
		#linearly interpolate between data points
		m = data[int(ceil(t))]-data[int(floor(t))]	#slope
		x = t%1	#dist from known value
		b = floor(t)	#known value
		return m*x + b
