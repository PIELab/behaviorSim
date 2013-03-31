from scipy import *
from pylab import *

from runParameters import *

	# these values are taken from verification simulation in section 3.2 of the following paper:
		#J.-Emeterio Navarro-Barrientos , Daniel E. Rivera & Linda M. Collins (2011):
		#A dynamical model for describing behavioural interventions for weight loss and body composition
		#change, Mathematical and Computer Modelling of Dynamical Systems: Methods, Tools and
		#Applications in Engineering and Related Sciences, 17:2, 183-203

class modelInput():

	# generalized step function (for use in defining input)
	def step(beforeStep,afterStep,stepTime,t):
		if t < stepTime:
			return beforeStep;
		else: # t > stepTime
			return afterStep;

	STEP_TIME = 3;	#time when step in input is applied

	# given belief step function
	def belief(t):
		return 4;
		#return step(4,6,STEP_TIME,t);
	
	# given outcome evaluation step function
	def outcomeEval(t):
		return 4;
		#return step(2,6,STEP_TIME,t);

	b1 = [belief(t) for t in range(timeToRun)];	#belief; strength of belief
	e1 = [outcomeEval(t) for t in range(timeToRun)];	#outcomeEval; evaluation of the outcome


	#behavioralBeliefCrossEvaluation; xi1; attitude towards behavior
	#normativeCrossMotivation;        xi2; subjective norms
	#controlBeliefCrossPower;         xi3; perceived behavioral control
	xi = array([[b1[t]*e1[t] for t in range(timeToRun)],	
		    [1           for t in range(timeToRun)],
		    [1           for t in range(timeToRun)]]);

	theta = array([0,0,0, 2,2,2,2,2]);	#time delays
	tau   = array([1,1,1, 2, 4]);		#time constants

	#exogenous inflow resistances:
	gamma = array([[1,1,1],\
		       [1,1,1],\
		       [1,1,1],\
		       [1,1,1],\
		       [1,1,1]]);

	#outflow resistance
	beta  = array([[0.5,0.5,0.5,0.5,0.5],\
		       [0.5,0.5,0.5,0.5,0.5],\
		       [0.5,0.5,0.5,0.5,0.5],\
		       [0.5,0.5,0.5,0.5,0.5],\
		       [0.5,0.5,0.5,0.5,0.5]]);

	# disturbances
	zeta= array([[0],\
	       [0],\
	       [0],\
	       [0],\
	       [0]]);


