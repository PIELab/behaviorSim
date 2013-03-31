# === === === === === === === === === === === === === === === === === ===
# runs a the model defined in oppropriate python files for one agent
# === === === === === === === === === === === === === === === === === ===

# import basic functions for calculation & plotting 
from scipy import *
from pylab import *

#show & save all relevant plots for given model, input
def makePlots(runTime,theModel,theInput, saveFileName):
	#initialize output lists...
	attitude = [0 for i in range(runParameters.timeToRun)];
	intention= [0 for i in range(runParameters.timeToRun)];
	behavior = [0 for i in range(runParameters.timeToRun)];
	PBC      = [0 for i in range(runParameters.timeToRun)];
	# get the info
	for t in range(runParameters.timeToRun):
		attitude[t] = theModel.stateHistory[t].attitude;
		intention[t]= theModel.stateHistory[t].intention;
		behavior[t] = theModel.stateHistory[t].behavior;
		PBC[t]      = theModel.stateHistory[t].PBC;

	subplots_adjust(wspace=0.6)
	subplots_adjust(hspace=0.6)

	#inputs on the left (odds)
	subplot(421)
	plot(theInput.xi[0]);
	ylabel('attitude (input; xi1)')
	ylim(0,90)
	grid(True)

	subplot(423)
	plot(theInput.xi[1]);
	ylabel('subjective norms in (xi2)')
	grid(True)

	subplot(425)
	plot(theInput.xi[2]);
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
	ylim(0,70)
	grid(True)

	subplot(426)
	plot(behavior);
	ylabel('behavior')
	ylim(0,50)
	grid(True)

	subplot(428)
	plot(PBC);
	#xlim(0,runParameters.timeToRun)
	#xlabel('time')
	ylabel('PBC')
	grid(True)

	#TODO: what about socialNorms?

	savefig(saveFileName);

import input_constant
constInput = input_constant.modelInput();	#input for the constant model
import firstOrderModel
constModel = firstOrderModel.modelInstance(constInput);


import input_firstOrderStep
firstInput = input_firstOrderStep.modelInput();	#input for the first order model
#firstOrderModel already imported
firstModel = firstOrderModel.modelInstance(firstInput);

#TODO:
#import secondOrderModel
#secondModel= secondOrderModel.modelInstance();
#import secondOrderModel
#secondModel = secondOrderModel.modelInstance(secondOrderInput);

import runParameters
for t in range(runParameters.timeToRun):
	constModel.iterate(constInput);	#run functions for each iteration
	firstModel.iterate(firstInput);

#TODO:
#	secondModel.iterate();

# === show plots
makePlots(runParameters.timeToRun,constModel,constInput,'figures/constModel');
makePlots(runParameters.timeToRun,firstModel,firstInput,'figures/firstOrderModel');
makePlots(runParameters.timeToRun,firstModel,firstInput,'figures/firstOrderModel');

savefig('allModels');
show();
