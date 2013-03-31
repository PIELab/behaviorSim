from scipy import *
from pylab import *

from agentState import *
import runParameters

# model instance contains all data needed to run a model
class modelInstance:
	#time values, T
	currentTime = 0; 		#assumed start at 0, deltaT = 1
	timeToRun = runParameters.timeToRun;
	currentState = None;
	stateHistory = None;

	def __init__(self,modelInput):
		# inputs, X
		# these are defined in input_<???>.py

		# outputs, Y

		# state variables, Z:
		self.currentState = agentState(modelInput);
		self.stateHistory = [ agentState(modelInput) for i in range(self.timeToRun)];	#set up state history to be filled

		# W

		# XX

		# YY

		# ZZ

		# F

		# H

		#G

	def iterate(self,modelInput):
		t = self.currentTime; #for easy formulas
		self.stateHistory[t].setState(self.currentState);

		#from eqtn 10 & 11 in 2010 Navarro-Barrientos et al @ CSEL
		GAMMA = modelInput.gamma;
		BETA  = modelInput.beta;
		XI    = modelInput.xi;
		THETA = modelInput.theta;
		TAU   = modelInput.tau;
		ZETA  = modelInput.zeta;

		#xi  = array([[modelInput.attitude[t]],\
		#       [modelInput.socialNorms[t]],\
		#       [modelInput.PBC[t]]]);

		# use this to get eta values at t<=now (in the past) 
		def eta(etaIndex, time):
			if etaIndex == 0:
				return self.stateHistory[time].attitude;
			elif etaIndex == 1:
				return self.stateHistory[time].socialNorms;
			elif etaIndex == 2:
				return self.stateHistory[time].PBC;
			elif etaIndex == 3:
				return self.stateHistory[time].intention;
			elif etaIndex == 4:
				return self.stateHistory[time].behavior;

		# print '\n',self.stateHistory[t].attitude,'\n'

		# ALL INDICIES FIXED TO START AT 0
		etaDot = [(GAMMA[0,0]*XI[0,t-THETA[0]] - eta(0,t) + ZETA[0])/TAU[0],\
		          (GAMMA[1,1]*XI[1,t-THETA[1]] - eta(1,t) + ZETA[1])/TAU[1],\
		          (GAMMA[2,2]*XI[2,t-THETA[2]] - eta(2,t) + ZETA[2])/TAU[2],\
		          (   BETA[3,0]*eta(0,t-THETA[3]) \
		            + BETA[3,1]*eta(1,t-THETA[4]) \
		            + BETA[3,2]*eta(2,t-THETA[5]) -eta(3,t)+ ZETA[3])/TAU[3],\
		          (   BETA[4,3]*eta(3,t-THETA[6]) \
		            + BETA[4,2]*eta(2,t-THETA[7]) - eta(4,t) + ZETA[4])/TAU[4]];

		#print BETA, '\n\n', eta,'\n\n',GAMMA,'\n\n',xi,'\n\n',zeta,'\n\n'
		#print BETA.shape,'x',eta.shape,'+',GAMMA.shape,'x',xi.shape,'+',zeta.shape

		# 1x5         5x5 * 1x5       3x5 * 1x3    1x5
#		nextEta = np.dot(BETA,eta) + np.dot(GAMMA,XI) + modelInput.zeta;

			# the most recent eta values:
		ETA = array([[self.stateHistory[t].attitude],\
		             [self.stateHistory[t].socialNorms],\
		             [self.stateHistory[t].PBC],\
		             [self.stateHistory[t].intention],\
		             [self.stateHistory[t].behavior]]);

		nextEta = ETA + etaDot;

		#NOTE: I don't really understand why the extra [0] is needed here, but I guess it is...t
		self.currentState.attitude    = nextEta[0][0];
		self.currentState.socialNorms = nextEta[1][0];
		self.currentState.PBC         = nextEta[2][0];
		self.currentState.intention   = nextEta[3][0];
		self.currentState.behavior    = nextEta[4][0];

		self.currentTime += 1;
		return;		
