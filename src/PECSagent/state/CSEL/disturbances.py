import random

from pylab import array

# gaussian random disturbances
# method metadata:
	# time-invariant? = TRUE
	# (sim)time-dependent? = FALSE
# requirements for this method to be valid:
	# requiredTimeScale = null
	# requiredTimeStep  = null
def gaussZeta(t):
	N = 5 #number of 'zetas'
	mean = 0
	stdDev = .02
	return  array([random.gauss(mean,stdDev) for n in range(0,N)])
