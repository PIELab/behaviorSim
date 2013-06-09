import random

# gaussian random disturbances
# method metadata:
	# time-invariant? = TRUE
	# (sim)time-dependent? = FALSE
# requirements for this method to be valid:
	# requiredTimeScale = null
	# requiredTimeStep  = null
def gaussZeta(data,t):
	if t < len(data):
		return data[t]
	else:
		N = 5 #number of 'zetas'
		if len(data) == 0:
			data.append([0.0]*N)
		mean = 0
		stdDev = .03
		for i in range(len(data),t+1):
			data.append([random.gauss(mean,stdDev) for n in range(0,N)])
		return data[t]
