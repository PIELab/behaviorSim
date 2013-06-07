
# gets the amount of fluid in the 'behavior' tank, eta_5. This state variable passes through unchanged, thus interpreting the value of the CSEL behavior tank as the motive to perform targeted action.
# method metadata:
	# time-invariant? = TRUE
	# (sim)time-dependent? = FALSE
# requirements for this method to be valid:
	# requiredTimeScale = null
	# requiredTimeStep  = null
def etaFive(data,t,eta):
	if t < len(data):
		return data[t]
	else:	# fill in data up to t
		for i in range(len(data),t+1):
			fullness = eta(i)[4]
			data.append(fullness)
	return data[t]

