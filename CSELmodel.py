# import basic functions for calculation & plotting 
from scipy import *
from pylab import *

#TODO: import definitions for each component?
import PECSinput

class agentState:
	#'endogeneous flow variables' from 2010 Navarro-Barrientos et al @ CSEL:
	attitude = 0;		#eta1; attitude towards behavior
	socialNorms = 0;	#eta2; subjective norms
	PBC = 0;		#eta3; perceived Behavioral Control
	intention = 0;		#eta4;
	behavior = 0;		#eta5;

	#TODO: inlude something like 'def init(self, initState)' to initialize all state vars to given state
	def setState(self, newState):
		self.attitude    = newState.attitude;
		self.socialNorms = newState.socialNorms;
		self.PBC         = newState.PBC;		
		self.intention   = newState.intention;		
		self.behavior    = newState.behavior;		
		

# model instance contains all data needed to run a model
class modelInstance:
	#time values, T
	currentTime = 0;
	timeToRun = PECSinput.timeToRun;	
	#assumed start at 0, deltaT = 1

	# inputs, X
	# these are defined in PECSinputs.py

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
		GAMMA = PECSinput.gamma;
		BETA  = PECSinput.beta;

		xi  = array([[PECSinput.attitude[t]],\
		       [PECSinput.socialNorms[t]],\
		       [PECSinput.PBC[t]]]);

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

# === === === === === === === === === === === === === === === === === ===
# runModel runs a the model defined in oppropriate python files for one agent
# === === === === === === === === === === === === === === === === === ===
thisModel = modelInstance();
for t in range(thisModel.timeToRun):
	thisModel.iterate();	#run functions for each iteration


# === show plots
time = range(thisModel.timeToRun);

#initialize output lists...
attitude = [0 for i in range(thisModel.timeToRun)];
intention= [0 for i in range(thisModel.timeToRun)];
behavior = [0 for i in range(thisModel.timeToRun)];
PBC      = [0 for i in range(thisModel.timeToRun)];
# get the info
for t in range(thisModel.timeToRun):
	attitude[t] = thisModel.stateHistory[t].attitude;
	intention[t]= thisModel.stateHistory[t].intention;
	behavior[t] = thisModel.stateHistory[t].behavior;
	PBC[t]      = thisModel.stateHistory[t].PBC;

subplots_adjust(wspace=0.6)

#inputs on the left (odds)
subplot(421)
plot(PECSinput.belief);
ylabel('belief')
grid(True)

subplot(423)
plot(PECSinput.attitude);
ylabel('attitude in')
grid(True)

subplot(425)
plot(PECSinput.socialNorms);
ylabel('social norms in')
grid(True)

subplot(427)
plot(PECSinput.PBC);
ylabel('PBC in')
grid(True)

#outputs on the right (evens)
subplot(422)
plot(attitude);
ylabel('attitude')
grid(True)

subplot(424)
plot(intention);
ylabel('intention')
grid(True)

subplot(426)
plot(behavior);
ylabel('behavior')
grid(True)

subplot(428)
plot(PBC);
#xlim(0,thisModel.timeToRun)
#xlabel('time')
ylabel('PBC')
grid(True)

#TODO: what about socialNorms?


savefig('figures/CSELmodelOutput');
show();



