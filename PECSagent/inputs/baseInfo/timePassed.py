# get amount of time given timeStep and iterations
	# time-invariant? = TRUE
	# (sim)time-dependent? = TRUE	(time==time!) ;)
# requirements for this method to be valid:
	# requiredTimeScale = null
	# requiredTimeStep  = null
def timePassed(data,index,deltaT):
	if index < len(data):
		return data[index]
	else:	# fill in data up to t
		if len(data) == 0:
			data.append(0)
		for i in range(len(data),index+1):
			time = data[i-1]+deltaT
			data.append(time)
	return data[index]

