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
	plot(time,ETA[1][:,0]);
	ylabel('soc. norm (eta2)')
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
print ' sample frequency: 1 /',deltaT,' days\n'

from time import time #for measuring model run time

# === CONSTANT 1ST ORDER
print 'running 1st order model with constant input...'
import model_firstorder, inputs_constant, agent_default
start = time()
constModel = model_firstorder.model(runParams,inputs_constant.inputs(),agent_default.agent())
print 'done. Time to complete:', time()-start, 's\n'

# plot this now, since next run of model_firstorder.model() seems to overwrite ETA... TODO: fix this
figure()
legend(( 'Simple plot', ) )
makePlots(constModel.ETA, constModel.theInput.xi, constModel.time)

# === STEP 1ST ORDER
print 'running 1st order model with step input...'
import inputs_step_1storder#, model_firstorder, agent_default
start = time()
firstModel = model_firstorder.model(runParams,inputs_step_1storder.inputs(),agent_default.agent())
print 'done. Time to complete:', time()-start, 's\n'

# === STEP 2ND ORDER
print 'running 2nd order model with step input...'
import model_secondorder, inputs_step_2ndorder#, agent_default
start = time()
secondModel = model_secondorder.model(runParams,inputs_step_2ndorder.inputs(),agent_default.agent())
print 'done. Time to complete:', time()-start, 's\n'

#ETA1= ETA[:,0]

#print 'SIZE'
#print size(ETA[0][:,0])

print 'Creating plots for your enjoyment...'
makePlots(firstModel.ETA, firstModel.theInput.xi, firstModel.time)
makePlots(secondModel.ETA,secondModel.theInput.xi,secondModel.time)
show()

print 'done.'
#savefig('figures/CSELmodels');

