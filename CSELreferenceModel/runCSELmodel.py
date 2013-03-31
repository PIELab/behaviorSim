# import basic functions for calculation & plotting 
from scipy import *
from pylab import *

#TODO: import definitions for each component?

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
subplots_adjust(hspace=0.6)

import firstOrderInput
#inputs on the left (odds)
subplot(421)
plot(firstOrderInput.xi[0]);
ylabel('attitude (input; xi1)')
grid(True)

subplot(423)
plot(firstOrderInput.xi[1]);
ylabel('subjective norms in (xi2)')
grid(True)

subplot(425)
plot(firstOrderInput.xi[2]);
ylabel('PBC in (xi3)')
grid(True)

subplot(427)
plot(0);
ylabel('empty graph')
grid(True)

#outputs on the right (evens)
subplot(422)
plot(attitude);
ylabel('attitude')
ylim(0,90)
grid(True)

subplot(424)
plot(intention);
ylabel('intention')
ylim(0,90)
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

