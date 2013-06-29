# get amount of time given timeStep and iterations
	# time-invariant? = TRUE
	# (sim)time-dependent? = TRUE	(time==time!) ;)
# requirements for this method to be valid:
	# requiredTimeScale = null
	# requiredTimeStep  = null
def timePassed(t,t_0,deltaT):
	return t_0+t*deltaT

