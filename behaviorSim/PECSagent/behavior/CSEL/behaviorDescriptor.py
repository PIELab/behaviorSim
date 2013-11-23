# this set of output methods creates a set of descriptors of user behavior which occur simultaneously. This is designed so that continuous models behavior such as the CSEL implementation for eating behavior and physical activity can express simultaneously.

# gets the names of the output variables:
def outputKey(t):
	return ['PhysicalActivity','EatingBehavior']

# This method is meant to act as a temporary filler for testing purposes. 
# It gets the amount of fluid in the physical Activity and eating behavior 
# fluid tanks, i.e., eta_5 This state variable passes through unchanged. 
# method metadata:
	# time-invariant? = TRUE
	# (sim)time-dependent? = FALSE
# requirements for this method to be valid:
	# requiredTimeScale = null
	# requiredTimeStep  = null
def outputValues(t,eta_PA,eta_EB):
	PAfullness = eta_PA(t)[4]
	EBfullness = eta_EB(t)[4]
	return[PAfullness,EBfullness]

