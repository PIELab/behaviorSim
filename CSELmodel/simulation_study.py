# -*- coding: utf-8 -*-
from pylab import * # for plotting commands & numpy array & normal()

#show & save all relevant plots for given model, input
def makePlots(ETA,xi,time):
	subplots_adjust(wspace=0.6)
	subplots_adjust(hspace=0.6)

	#inputs on the left (odds)
	subplot(421)
	plot(time,[ xi(t*deltaT)[0] for t in range (runParams.N_SAMPLES) ]);
	ylabel('attitude in (xi1)')
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
	grid(True)

	subplot(424)
	plot(time,ETA[3][:,0]);
	ylabel('intention (eta4)')
	grid(True)

	subplot(426)
	plot(time,ETA[4][:,0]);
	ylabel('behavior (eta5)')
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
	END_TIME   = 180.0
	N_SAMPLES  = 1001

runParams = runParameters()

#time window:
deltaT = abs(runParams.END_TIME-runParams.START_TIME)/runParams.N_SAMPLES;	#time step

print 'model start(days):',runParams.START_TIME
print '  model end(days):',runParams.END_TIME
print 'number of samples:',runParams.N_SAMPLES
print ' sample frequency: 1 /',deltaT,' days\n'

from time import time #for measuring model run time

print ' === Physical Activity Models === '
# plot this now, since next run of model_firstorder.model() seems to overwrite ETA... TODO: fix this
figure('pysical activity')
legend(( 'Simple plot', ) )#note: this doesn't seem to do anything...

print 'running agent i 1st order model for pysical activity...'
from model_firstorder import model
from inputs_simulation_activity import inputs
from agent_simulation_i import agent
start = time()
PAmodeli = model(runParams,inputs(),agent())
print 'done. Time to complete:', time()-start, 's\n'
makePlots(PAmodeli.ETA, PAmodeli.theInput.xi, PAmodeli.time)

print 'running agent ii 1st order model for pysical activity...'
from agent_simulation_ii import agent
start = time()
PAmodelii = model(runParams,inputs(),agent())
print 'done. Time to complete:', time()-start, 's\n'
makePlots(PAmodelii.ETA, PAmodelii.theInput.xi, PAmodelii.time)

print 'running agent iii 1st order model for pysical activity...'
from agent_simulation_iiiactivity import agent
start = time()
PAmodeliii = model(runParams,inputs(),agent())
print 'done. Time to complete:', time()-start, 's\n'

#add disturbances for agent iii
maxV = 20	# maximum value
minV = 0	# minimum value
maxAmplitude = .03	# max of disturbance
mean = 0
stdDev = .03
cpy = [PAmodeliii.ETA[0][i,0] for i in range(runParams.N_SAMPLES)]
for i in range(runParams.N_SAMPLES-1):	
	#dist = (0.5-random())*2.0 * maxAmplitude	#flat random disturbances
	dist = normal(mean,stdDev,1)	#gaussian disturbances
	#make sure resulting eta will be within bounds
	if PAmodeliii.ETA[0][i,0] + dist >= maxV:
		dist = -1.0
	elif PAmodeliii.ETA[0][i,0] + dist <= minV:
		dist = 1.0
	else:
		dist = dist
	print PAmodeliii.ETA[0][i-1,0],'=?=',cpy[i-1]
	PAmodeliii.ETA[0][i,0] = PAmodeliii.ETA[0][i,0] + dist + (PAmodeliii.ETA[0][i-1,0]-cpy[i-1])

makePlots(PAmodeliii.ETA, PAmodeliii.theInput.xi, PAmodeliii.time)

print ' === Eating Behavior Models === '
figure('eating behavior')

print 'running agent i 1st order model for eating behavior...'
from model_firstorder import model
from inputs_simulation_eating import inputs
from agent_simulation_i import agent
start = time()
EBmodeli = model(runParams,inputs(),agent())
print 'done. Time to complete:', time()-start, 's\n'
makePlots(EBmodeli.ETA, EBmodeli.theInput.xi, EBmodeli.time)

print 'running agent ii 1st order model for eating behavior...'
from agent_simulation_ii import agent
start = time()
EBmodelii = model(runParams,inputs(),agent())
print 'done. Time to complete:', time()-start, 's\n'
makePlots(EBmodelii.ETA, EBmodelii.theInput.xi, EBmodelii.time)

print 'running agent iii 1st order model for eating behavior...'
from agent_simulation_iiieating import agent
start = time()
EBmodeliii = model(runParams,inputs(),agent())
print 'done. Time to complete:', time()-start, 's\n'
#add disturbances for agent iii
maxV = 50	# maximum value
minV = 0	# minimum value
maxAmplitude = .03	# max of disturbance
mean = 0
stdDev = .03
cpy = [EBmodeliii.ETA[0][i,0] for i in range(runParams.N_SAMPLES)]
for i in range(runParams.N_SAMPLES-1):	
	#dist = (0.5-random())*2.0 * maxAmplitude	#flat random disturbances
	dist = normal(mean,stdDev,1)	#gaussian disturbances
	#make sure resulting eta will be within bounds
	if EBmodeliii.ETA[0][i,0] + dist >= maxV:
		dist = -1.0
	elif EBmodeliii.ETA[0][i,0] + dist <= minV:
		dist = 1.0
	else:
		dist = dist
	print EBmodeliii.ETA[0][i-1,0],'=?=',cpy[i-1]
	EBmodeliii.ETA[0][i,0] = EBmodeliii.ETA[0][i,0] + dist + (EBmodeliii.ETA[0][i-1,0]-cpy[i-1])

makePlots(EBmodeliii.ETA, EBmodeliii.theInput.xi, EBmodeliii.time)

#ETA1= ETA[:,0]

#print 'SIZE'
#print size(ETA[0][:,0])

print 'Creating plots for your enjoyment...'
show()

print 'done.'
#savefig('figures/CSELmodels');

