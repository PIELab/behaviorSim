# this set of output methods creates a set of descriptors of user behavior which occur simultaneously. This is designed so that continuous models behavior such as the CSEL implementation for eating behavior and physical activity can express simultaneously.

# gets the names of the output variables:
def outputKeys(data,t):
	return ['PhysicalActivity','EatingBehavior']

# This method is meant to act as a temporary filler for testing purposes. It gets the amount of fluid in the physical Activity and eating behavior fluid tanks, i.e., eta_5 This state variable passes through unchanged. 
# method metadata:
	# time-invariant? = TRUE
	# (sim)time-dependent? = FALSE
# requirements for this method to be valid:
	# requiredTimeScale = null
	# requiredTimeStep  = null
def outputValues(data,t,eta):
	if t < len(data):
		return data[t]
	else:	# fill in data up to t
		for i in range(len(data),t+1):
			PAfullness = eta(i)[4]
			EBfullness = 0	#TODO: actually make this work..
			data.append([PAfullness,EBfullness])
	return data[t]
