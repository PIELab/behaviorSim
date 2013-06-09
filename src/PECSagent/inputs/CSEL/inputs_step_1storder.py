#class to define all inputs into the model based on step function for 1st order model in figure 7 of the following article:

#J.-Emeterio Navarro-Barrientos , Daniel E. Rivera & Linda M. Collins (2011):
#A dynamical model for describing behavioural interventions for weight loss and body composition
#change, Mathematical and Computer Modelling of Dynamical Systems: Methods, Tools and
#Applications in Engineering and Related Sciences, 17:2, 183-203


from pylab import array

class inputs:
	# given belief step function
	def belief(self,t):
		stepTime = 3;
		beforeStep = 4;
		afterStep = 6;
		if t < stepTime:
			return beforeStep;
		else: # t > stepTime
			return afterStep;

	# given outcome evaluation step function
	def outcomeEval(self,t):
		stepTime = 3;
		beforeStep = 2;
		afterStep = 6;
		if t < stepTime:
			return beforeStep;
		else: # t > stepTime
			return afterStep;

	def xi(self,t):
		return array([self.belief(t)*self.outcomeEval(t), 1, 1]);	#xi_2 & xi_3 are const. here...
#	xi = array([[b1[t]*e1[t] for t in range(timeToRun)],	
#		    [1           for t in range(timeToRun)],
#		    [1           for t in range(timeToRun)]]);
