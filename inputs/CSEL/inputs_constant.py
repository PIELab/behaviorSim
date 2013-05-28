#class to define all inputs into the model

from pylab import array

class inputs:
	# belief function
	def belief(self,t):
		return 4;
	# outcome evaluation function
	def outcomeEval(self,t):
		return 2;
	# exogenous flow vars
	def xi(self,t):
		return array([self.belief(t)*self.outcomeEval(t), 1, 1]);	#xi_2 & xi_3 are const. here...
