#class to define all inputs into the model

from pylab import array

# belief function
def belief(t):
	return 4
def getBelief():
	return belief

# outcome evaluation function
def outcomeEval(t):
	return 2
def getOutcomeEval():
	return outcomeEval

# exogenous flow vars
def xi(t):
	return array([belief(t)*outcomeEval(t), 1, 1])	#xi_2 & xi_3 are const. here...
def getXi():
	return xi
