from pylab import array

# belief function reflects the subject's beliefs about an action. 
# Constant belief function indicates no change in agent beliefs
	# time-invariant? = TRUE
	# (sim)time-dependent? = FALSE
# requirements for this method to be valid:
	# requiredTimeScale = null
	# requiredTimeStep  = null
def belief(data,t):
	return 4;

# outcome evaluation function 
# Constant function indicates no change in agent beliefs
	# time-invariant? = TRUE
	# (sim)time-dependent? = FALSE
# requirements for this method to be valid:
	# requiredTimeScale = null
	# requiredTimeStep  = null
def outcomeEval(data,t):
	return 2;

# exogenous flow vars
# Constant function indicates no change in agent beliefs
	# time-invariant? = TRUE
	# (sim)time-dependent? = FALSE
# requirements for this method to be valid:
	# requiredTimeScale = null
	# requiredTimeStep  = null
def xi(data,t,belief_t,outcomeEval_t):
	return array([belief_t*outcomeEval_t, 1, 1]);	#xi_2 & xi_3 are const. here...
