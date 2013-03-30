# import basic functions for calculation & plotting 
from scipy import *
from pylab import *

#TODO: import definitions for each component?
import PECSinput

# === === === === === === === === === === === === === === === === === ===
# runModel runs a the model defined in oppropriate python files for one agent
# === === === === === === === === === === === === === === === === === ===
import firstOrderModel
#import secondOrderModel

firstModel = firstOrderModel.modelInstance();
#secondModel= secondOrderModel.modelInstance();

import runParameters
for t in range(runParameters.timeToRun):
	firstModel.iterate();	#run functions for each iteration
#	secondModel.iterate();

# === show plots
time = range(runParameters.timeToRun);

#initialize output lists...
attitude = [0 for i in range(runParameters.timeToRun)];
intention= [0 for i in range(runParameters.timeToRun)];
behavior = [0 for i in range(runParameters.timeToRun)];
PBC      = [0 for i in range(runParameters.timeToRun)];
# get the info
for t in range(runParameters.timeToRun):
	attitude[t] = firstModel.stateHistory[t].attitude;
	intention[t]= firstModel.stateHistory[t].intention;
	behavior[t] = firstModel.stateHistory[t].behavior;
	PBC[t]      = firstModel.stateHistory[t].PBC;

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
#xlim(0,runParameters.timeToRun)
#xlabel('time')
ylabel('PBC')
grid(True)

#TODO: what about socialNorms?


savefig('figures/CSELmodelOutput');
show();

