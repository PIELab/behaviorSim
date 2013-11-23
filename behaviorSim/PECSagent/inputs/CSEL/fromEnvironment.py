#this file defines methods for retrieving information from the agent's environment

# returns influence on physical activity attitude
	# time-invariant? = TRUE
	# (sim)time-dependent? = FALSE
# requirements for this method to be valid:
	# requiredTimeScale = null
	# requiredTimeStep  = null
def pa(t,influence_PA):
	return influence_PA(t)

def eb(t,influence_EB):
	return influence_EB(t)
