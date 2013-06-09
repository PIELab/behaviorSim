from ....__util.attitude import attitude

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
