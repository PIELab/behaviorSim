# get amount of time given timeStep and iterations
	# time-invariant? = TRUE
	# (sim)time-dependent? = TRUE	(time==time!) ;)
# requirements for this method to be valid:
	# requiredTimeScale = null
	# requiredTimeStep  = null
def timePassed(timeFunc,t,t_0,deltaT):
	if t == 0:
		return t_0
	else:
		return timeFunc(t-1)+deltaT

