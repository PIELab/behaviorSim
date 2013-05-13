#class to define all inputs into the model based on step function for 1st order model in figure 7 of the following article:

#J.-Emeterio Navarro-Barrientos , Daniel E. Rivera & Linda M. Collins (2011):
#A dynamical model for describing behavioural interventions for weight loss and body composition
#change, Mathematical and Computer Modelling of Dynamical Systems: Methods, Tools and
#Applications in Engineering and Related Sciences, 17:2, 183-203


from pylab import array
from math import floor

class inputs:
	# given belief step function
	def belief(self,t):
		#return step(t, 2,1,3)
		return squareWave(t, 3, 1, 1) 

	# given outcome evaluation step function
	def outcomeEval(self,t):
		return 1;

	# xi = [ attitude, social norm, planned behavioral control ]
	def xi(self,t):
		return array([self.belief(t)*self.outcomeEval(t),
		              1,
		              1]);	#xi_2 & xi_3 are const here...
#	xi = array([[b1[t]*e1[t] for t in range(timeToRun)],	
#		    [1           for t in range(timeToRun)],
#		    [1           for t in range(timeToRun)]]);

#defines a step function at stepTime
def step(t, stepTime, beforeStep, afterStep):
	if t < stepTime:
		return beforeStep;
	else: # t > stepTime
		return afterStep;

#defines square wave starting (high) at t=0 with given high and low and frequency in 1/t units
# NOTE: 'high' is not required to be lower than 'low', changing this changes intial behavior i.e. |-_-_-| vs |_-_-_|
def squareWave(t, high, low, frequency):
	if ( (floor(t/frequency)) % 2 == 0 ):
		return low
	else:
		return high

