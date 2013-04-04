# -*- coding: utf-8 -*-
from pylab import * # for plotting commands & array

#show & save all relevant plots for given model, input
def makePlots(ETA,xi):
	figure()
	subplots_adjust(wspace=0.6)
	subplots_adjust(hspace=0.6)

	#inputs on the left (odds)
	subplot(421)
	plot([ xi(t*deltaT)[0] for t in range (runParams.N_SAMPLES) ]);
	ylabel('attitude (input; xi1)')
	ylim(0,90)
	grid(True)

	subplot(423)
	plot(0);
	ylabel('subjective norms in (xi2)')
	grid(True)

	subplot(425)
	plot(0);
	ylabel('PBC in (xi3)')
	grid(True)

	subplot(427)
	plot(0);
	ylabel('empty graph')
	grid(True)

	#outputs on the right (evens)
	subplot(422)
	plot(ETA[0][:,0]);
	ylabel('attitude (eta1)')
	ylim(0,90)
	grid(True)

	subplot(424)
	plot(ETA[3][:,0]);
	ylabel('intention (eta4)')
	ylim(0,70)
	grid(True)

	subplot(426)
	plot(ETA[4][:,0]);
	ylabel('behavior (eta5)')
	ylim(0,50)
	grid(True)

	subplot(428)
	plot(ETA[2][:,0]);
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



import firstOrderModel
firstModel = firstOrderModel.firstOrderModel(runParams)

ETA = firstModel.ETA;
time= firstModel.time;

#ETA1= ETA[:,0]

#print 'SIZE'
#print size(ETA[0][:,0])

#firstOrderModel.getEtaConsts()	#gets xi to this level for makePlots
makePlots(ETA,firstModel.xi)
#savefig('figures/CSELmodels');

#another plot:
figure()
#ylim(0,90)
grid(True)
for i in range(5):
	plot(time,ETA[i][:,0])
xlabel('t')
ylabel('eta')
show()
