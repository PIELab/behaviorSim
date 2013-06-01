from datetime import datetime

# gets the mortality (suceptibility to death) based on sim-world age of an agent
# method metadata:
	# time-invariant? = TRUE
	# (sim)time-dependent? = TRUE
# requirements for this method to be valid:
	# requiredTimeScale = null
	# requiredTimeStep  = null
def oldAger(data,t,age):
	if t < len(data):
		return data[t]
	else:	# fill in data up to t
		maxAge = 130
		for i in range(len(data),t+1):
			yearAge=age(t).total_seconds()/(60*60*24*365.242)
			mortality = yearAge/130
			data.append(mortality)
	return data[t]

	
