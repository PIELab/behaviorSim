from ...__util.attitude import attitude

from pylab import array
from math import floor

# returns a constant attitude as defined in __util.attitude 
	# time-invariant? = TRUE
	# (sim)time-dependent? = FALSE
# requirements for this method to be valid:
	# requiredTimeScale = null
	# requiredTimeStep  = null
def constAttitude(data, t):
	if t < len(data):
		return data[t]
	else:
		a = attitude()
		a.behavioralBelief = 1
		a.behaviorAttitude = 1
		a.normativeBelief  = 1
		a.subjectiveNorm   = 1
		a.PBC              = 1
		a.controlBelief    = 1

		if len(data) == 0:
			data.append(a)
		for i in range(len(data),t+1):
			data.append(a)
		return data[t]

# returns a various square waves for debugging 
	# time-invariant? = TRUE
	# (sim)time-dependent? = TRUE
# requirements for this method to be valid:
	# requiredTimeScale = null
	# requiredTimeStep  = null
def squareWaves(data, t):
	if t < len(data):
		return data[t]
	else:
		for i in range(len(data),t+1):
			a = attitude()
			a.behavioralBelief = squareWave(t,.9,.1,1)
			a.behaviorAttitude = squareWave(t,.9,.1,2)
			a.normativeBelief  = squareWave(t,.9,.1,3)
			a.subjectiveNorm   = squareWave(t,.9,.1,4)
			a.PBC              = squareWave(t,.9,.1,5)
			a.controlBelief    = squareWave(t,.9,.1,6)
			data.append(a)
		return data[t]

def someSteps(t):
	a = attitude()
	a.behavioralBelief = step(t,1  ,1,5)
	a.behaviorAttitude = step(t,10 ,4,2)
	a.normativeBelief  = step(t,20 ,5,6)
	a.subjectiveNorm   = step(t,15 ,2,4)
	a.PBC              = step(t,30 ,3,1)
	a.controlBelief    = step(t,100,7,3)
	return a


#defines a step function at stepTime
def step(t, stepTime, beforeStep, afterStep):
	if t < stepTime:
		return beforeStep;
	else: # t > stepTime
		return afterStep;

#defines square wave starting (high) at t=0 with given high and low and frequency in 1/t units
# NOTE: 'high' is not required to be lower than 'low', changing this changes intial behavior i.e. highstart:|-_-_-| vs lowstart:|_-_-_|
def squareWave(t, high, low, frequency):
	if ( (floor(t/frequency)) % 2 == 0 ):
		return low
	else:
		return high
