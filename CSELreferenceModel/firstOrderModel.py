from scipy import *
from pylab import *

import firstOrderInput
from agentState import *

# model instance contains all data needed to run a model
class modelInstance:
	#time values, T
	currentTime = 0;
	timeToRun = firstOrderInput.timeToRun;	
	#assumed start at 0, deltaT = 1

	# inputs, X
	# these are defined in firstOrderInputs.py

	# outputs, Y

	# state variables, Z:
	currentState = agentState();
	stateHistory = [ agentState() for i in range(timeToRun)];	#set up state history to be filled

	# W

	# XX

	# YY

	# ZZ

	# F

	# H

	#G

	def iterate(self):
		t = self.currentTime; #for easy formulas
		self.stateHistory[t].setState(self.currentState);

		#from eqtn 10 & 11 in 2010 Navarro-Barrientos et al @ CSEL
		GAMMA = firstOrderInput.gamma;
		BETA  = firstOrderInput.beta;

		xi  = array([[firstOrderInput.attitude[t]],\
		       [firstOrderInput.socialNorms[t]],\
		       [firstOrderInput.PBC[t]]]);

		eta = array([[self.stateHistory[t].attitude],\
		       [self.stateHistory[t].socialNorms],\
		       [self.stateHistory[t].PBC],\
		       [self.stateHistory[t].intention],\
		       [self.stateHistory[t].behavior]]);

		# print '\n',self.stateHistory[t].attitude,'\n'

		#TODO: calculate these disturbances
		zeta= array([[0],\
		       [0],\
		       [0],\
		       [0],\
		       [0]]);

		#print BETA, '\n\n', eta,'\n\n',GAMMA,'\n\n',xi,'\n\n',zeta,'\n\n'
		#print BETA.shape,'x',eta.shape,'+',GAMMA.shape,'x',xi.shape,'+',zeta.shape

		# 1x5         5x5 * 1x5       3x5 * 1x3    1x5
		nextEta = np.dot(BETA,eta) + np.dot(GAMMA,xi) + zeta;

		#NOTE: I don't really understand why the extra [0] is needed here, but I guess it is...t
		self.currentState.attitude    = nextEta[0][0];
		self.currentState.socialNorms = nextEta[1][0];
		self.currentState.PBC         = nextEta[2][0];
		self.currentState.intention   = nextEta[3][0];
		self.currentState.behavior    = nextEta[4][0];

		self.currentTime += 1;
		return;		
