#this file defines methods for retrieving information from the agent's environment

# returns influence on physical activity attitude
	# time-invariant? = TRUE
	# (sim)time-dependent? = FALSE
# requirements for this method to be valid:
	# requiredTimeScale = null
	# requiredTimeStep  = null
def pa(t,environment):
	return environment.influence_PA(t)

def eb(t,environment):
	return environment.influence_EB(t)
