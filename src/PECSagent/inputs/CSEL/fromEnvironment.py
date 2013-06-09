#this file defines methods for retrieving information from the agent's environment

# returns influence on physical activity attitude
	# time-invariant? = TRUE
	# (sim)time-dependent? = FALSE
# requirements for this method to be valid:
	# requiredTimeScale = null
	# requiredTimeStep  = null
def pa(data, t,environment):
	if t < len(data):
		return data[t]
	else:
		for i in range(len(data),t+1):
			a = environment.influence_PA(i)
			data.append(a)
		return data[t]
