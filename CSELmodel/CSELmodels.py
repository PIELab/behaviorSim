# -*- coding: utf-8 -*-
from pylab import * # for plotting commands & array

#show & save all relevant plots for given model, input
def makePlots(ETA,xi,time):
	subplots_adjust(wspace=0.6)
	subplots_adjust(hspace=0.6)

	#inputs on the left (odds)
	subplot(421)
	plot(time,[ xi(t*deltaT)[0] for t in range (runParams.N_SAMPLES) ]);
	ylabel('attitude (input; xi1)')
	ylim(0,90)
	grid(True)

	subplot(423)
	plot(time,[ xi(t*deltaT)[1] for t in range (runParams.N_SAMPLES) ]);
	ylabel('subjective norms in (xi2)')
	grid(True)

	subplot(425)
	plot(time,[ xi(t*deltaT)[2] for t in range (runParams.N_SAMPLES) ]);
	ylabel('PBC in (xi3)')
	grid(True)

	subplot(427)
	plot(time,time);
	ylabel('empty graph')
	grid(True)

	#outputs on the right (evens)
	subplot(422)
	plot(time,ETA[0][:,0]);
	ylabel('attitude (eta1)')
	ylim(0,90)
	grid(True)

	subplot(424)
	plot(time,ETA[3][:,0]);
	ylabel('intention (eta4)')
	ylim(0,70)
	grid(True)

	subplot(426)
	plot(time,ETA[4][:,0]);
	ylabel('behavior (eta5)')
	ylim(0,50)
	grid(True)

	subplot(428)
	plot(time,ETA[2][:,0]);
	#xlim(0,runParameters.timeToRun)
	#xlabel('time')
	ylabel('PBC (eta3)')
	grid(True)

	#TODO: what about socialNorms?


#run parameters:
class runParameters:
	START_TIME = 0.0
	END_TIME   = 35.0
	N_SAMPLES  = 1001

runParams = runParameters()

#time window:
deltaT = abs(runParams.END_TIME-runParams.START_TIME)/runParams.N_SAMPLES;	#time step

import firstOrderConstIn
constModel = firstOrderConstIn.firstOrderConstIn(runParams)
import firstOrderModel
firstModel = firstOrderModel.firstOrderModel(runParams)
#TODO:
import secondOrderModel
secondModel = secondOrderModel.secondOrderModel(runParams)

#ETA1= ETA[:,0]

#print 'SIZE'
#print size(ETA[0][:,0])

figure()
legend(( 'Simple plot', ) )
makePlots(constModel.ETA,constModel.xi,constModel.time)
makePlots(firstModel.ETA,firstModel.xi,firstModel.time)
makePlots(secondModel.ETA,secondModel.xi,secondModel.time)
show()
#savefig('figures/CSELmodels');

#another plot:
#figure()
#ylim(0,90)
#grid(True)
#for i in range(5):
#	plot(time,ETA[i][:,0])
#xlabel('t')
#ylabel('eta')
#show()
