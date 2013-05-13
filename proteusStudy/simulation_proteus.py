# -*- coding: utf-8 -*-
from pylab import * # for plotting commands & numpy array & normal()
import matplotlib.pyplot as plt

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
	END_TIME   = 8.0
	N_SAMPLES  = 1001

runParams = runParameters()

#time window:
deltaT = abs(runParams.END_TIME-runParams.START_TIME)/runParams.N_SAMPLES;	#time step

print 'model start(days):',runParams.START_TIME
print '  model end(days):',runParams.END_TIME
print 'number of samples:',runParams.N_SAMPLES
print ' sample frequency: 1 /',deltaT,' days\n'

from time import time #for measuring model run time

n_iAgents = 50 # number of intermediate agents to generate

fig = plt.figure('pysical activity')
NUM_COLORS = n_iAgents
colorCycle = [plt.get_cmap('RdBu_r')(1.*i/NUM_COLORS) for i in range(NUM_COLORS)]
ax = fig.add_subplot(421)
ax.set_color_cycle(colorCycle)
ax = fig.add_subplot(422)
ax.set_color_cycle(colorCycle)
ax = fig.add_subplot(423)
ax.set_color_cycle(colorCycle)
ax = fig.add_subplot(424)
ax.set_color_cycle(colorCycle)
ax = fig.add_subplot(425)
ax.set_color_cycle(colorCycle)
ax = fig.add_subplot(426)
ax.set_color_cycle(colorCycle)
ax = fig.add_subplot(427)
ax.set_color_cycle(colorCycle)
ax = fig.add_subplot(428)
ax.set_color_cycle(colorCycle)


print ' === Physical Activity Models === '
#legend(( 'Simple plot', ) )#note: this doesn't seem to do anything...

print 'running agent i (quick-adapter) 1st order model for pysical activity...'
from model_firstorder import model
from inputs_proteusSocialNormChange import inputs	#TODO: is this the right way of showing proteus input?
from agent_simulation_i import agent
start = time()
PAmodeli = model(runParams,inputs(),agent())
print 'done. Time to complete:', time()-start, 's\n'
makePlots(PAmodeli.ETA, PAmodeli.theInput.xi, PAmodeli.time)

print 'running generated intermediate agents...'
#this runs generated agents between agent i and ii
from agent_simulation_i import agent as a1
from agent_simulation_ii import agent as a2
for i in range(n_iAgents):
	print 'generated agent #', i,'\n'
	agent.theta += (a2.theta -a1.theta)/n_iAgents
	agent.tau   += (a2.tau   -a1.tau  )/n_iAgents
	agent.beta  += (a2.beta  -a1.beta )/n_iAgents
	start = time()
	iModel = model(runParams,inputs(),agent())
	print 'done. Time to complete:', time()-start, 's\n'
	makePlots(iModel.ETA, iModel.theInput.xi, iModel.time)
	# gamma is constant; tauA & sigma & zeta unused

print 'running agent ii (resistant to change) 1st order model for pysical activity...'
from agent_simulation_ii import agent
start = time()
PAmodelii = model(runParams,inputs(),agent())
print 'done. Time to complete:', time()-start, 's\n'
makePlots(PAmodelii.ETA, PAmodelii.theInput.xi, PAmodelii.time)

print 'Creating plots for your enjoyment...'
show()

print 'done.'
#savefig('figures/CSELmodels');

