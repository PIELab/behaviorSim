
# gets the amount of fluid in the 'behavior' tank, i.e., eta_5 (I think) This state variable passes through unchanged.
# method metadata:
	# time-invariant? = TRUE
	# (sim)time-dependent? = FALSE
# requirements for this method to be valid:
	# requiredTimeScale = null
	# requiredTimeStep  = null
def xiFive(data,t,eta):
	if t < len(data):
		return data[t]
	else:	# fill in data up to t
		for i in range(len(data),t+1):
			fullness = eta(i)[4]
			data.append(fullness)
	return data[t]

