# -*- coding: utf-8 -*-
from pylab import * # for plotting commands & array

#show & save all relevant plots for given model, input
def makePlots(ETA,xi,time):
	subplots_adjust(wspace=0.6)
	subplots_adjust(hspace=0.6)

	#inputs on the left (odds)
	subplot(421)
	plot(time,[ xi(t*deltaT)[0] for t in range (runParams.N_SAMPLES) ]);
	ylabel('attitude in (xi1)')
	ylim(0,90)
	grid(True)

	subplot(423)
	plot(time,[ xi(t*deltaT)[1] for t in range (runParams.N_SAMPLES) ]);
	ylabel('soc. norms in (xi2)')
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

	#another way to plot them:
	#figure()
	#ylim(0,90)
	#grid(True)
	#for i in range(5):
	#	plot(time,ETA[i][:,0])
	#xlabel('t')
	#ylabel('eta')
	#show()



print ' === Agent modeling coded by USF PIE-Lab based on ASU CSEL behavior simulation === '

#run parameters:
class runParameters:
	START_TIME = 0.0
	END_TIME   = 35.0
	N_SAMPLES  = 1001

runParams = runParameters()

#time window:
deltaT = abs(runParams.END_TIME-runParams.START_TIME)/runParams.N_SAMPLES;	#time step

print 'model start(days):',runParams.START_TIME
print '  model end(days):',runParams.END_TIME
print 'number of samples:',runParams.N_SAMPLES
print ' sample frequency: 1 /',deltaT,' days'

import inputs_constant, agent_default
# === INPUT:
theInput = inputs_constant.inputs()	# inputs to agent
theAgent = agent_default.agent()	# agent constants

print 'running 1st order model with constant input...'
import model_firstorder
constModel = model_firstorder.model(runParams,theInput,theAgent)

print 'running 1st order model with step input...'
import firstOrderModel	#TODO
firstModel = firstOrderModel.firstOrderModel(runParams)

print 'running 2nd order model with step input...'
import secondOrderModel	#TODO
secondModel = secondOrderModel.secondOrderModel(runParams)

#ETA1= ETA[:,0]

#print 'SIZE'
#print size(ETA[0][:,0])

print 'Creating plots for your enjoyment...'
figure()
legend(( 'Simple plot', ) )
makePlots(constModel.ETA,theInput.xi,constModel.time)
makePlots(firstModel.ETA,firstModel.xi,firstModel.time)
makePlots(secondModel.ETA,secondModel.xi,secondModel.time)
show()

print 'done.'
#savefig('figures/CSELmodels');

