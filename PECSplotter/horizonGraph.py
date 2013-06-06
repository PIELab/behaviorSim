# this file defines a set of functions for plotting the various attributes of a PECS agent

import datetime
import pylab
from .horizongraph_matplotlib.plugin import Horizon #for pretty plots

#plots inputs, state, motives, and output
def plotAll(agent,t0,tf):
	printAgentConstants(agent)
	plotInputs(agent,t0,tf)
	plotState(agent,t0,tf)
	plotMotive(agent,t0,tf)
#...

#prints out agent constants (agent personality)
def printAgentConstants(agent):
	print 'agent state constants (personality):'
	print 'name='+str(agent.state.name)
	print 'birthday='+str(agent.state.birthday)
	print 'theta='+str(agent.state.theta)
	print 'tau='+str(agent.state.theta)
	print 'gamma='+str(agent.state.gamma)
	print 'beta='+str(agent.state.beta)
	print 'tauA='+str(agent.state.tauA)
	print 'sigma='+str(agent.state.sigma)

#plots a given feature of behavior
def plotBehaviorFeature(feature,t0,tf):
	print 'NOT YET IMPLEMENTED!'

#plots all motives of the agent as time series from t0 to tf
def plotMotive(agent,t0,tf):
	print 'loading agent motive...'
	x = [(agent.inputs.time(t)-agent.inputs.time(0)).total_seconds() for t in range(t0,tf)]

	y = [[agent.motive.mortality(t) for t in range(t0,tf)],\
	     [agent.motive.will_PA(t) for t in range(t0,tf)]]

	labels = ['mortality','will_PA']

	N = 3	#number of bands
	
	print 'plotting agent motive...'
#	pylab.figure('agent '+str(agent.state.name)+' motive')
	
	plot = Horizon().run(x,y,labels,\
	                     figname='agent '+str(agent.state.name)+' motive',\
	                     bands=N)
	plot.subplots_adjust(left=0.07, right=0.998, top=0.99,bottom=0.01)


# plots all state of the agent as a time series from t0 to tf
def plotState(agent,t0,tf): 
	print 'loading agent state...'
	x =     [(agent.inputs.time(t)-agent.inputs.time(0)).total_seconds() for t in range(t0,tf)]

	y = [[agent.state.age(t).total_seconds()/(60*60*24*365.242) for t in range(t0,tf)],\
	     [agent.state.zeta(t)[0] for t in range(t0,tf)],\
	     [agent.state.zeta(t)[1] for t in range(t0,tf)],\
	     [agent.state.zeta(t)[2] for t in range(t0,tf)],\
	     [agent.state.zeta(t)[3] for t in range(t0,tf)],\
	     [agent.state.zeta(t)[4] for t in range(t0,tf)],\
	     [agent.state.eta(t)[0] for t in range(t0,tf)],\
	     [agent.state.eta(t)[1] for t in range(t0,tf)],\
	     [agent.state.eta(t)[2] for t in range(t0,tf)],\
	     [agent.state.eta(t)[3] for t in range(t0,tf)],\
	     [agent.state.eta(t)[4] for t in range(t0,tf)]]

	labels = ['age','zeta1','zeta2','zeta3','zeta4','zeta5','eta1','eta2','eta3','eta4','eta5']

	N = 3	#number of bands

	print 'plotting agent state...'

	plot = Horizon().run(x,y,labels,\
	                     figname='agent '+str(agent.state.name)+' state',\
	                     bands=N)
	plot.subplots_adjust(left=0.07, right=0.998, top=0.99,bottom=0.01)


# plots all inputs of the agent as a time series from t0 to tf
def plotInputs(agent,t0,tf): 
	print 'loading agent inputs...'
	x =     [(agent.inputs.time(t)-agent.inputs.time(0)).total_seconds() for t in range(t0,tf)]

	y = [[(agent.inputs.initTime(t)-datetime.datetime(datetime.MINYEAR,1,1)).total_seconds() for t in range(t0,tf)],\
	     [agent.inputs.PAbelief(t) for t in range(t0,tf)],\
	     [agent.inputs.PAoutcomeEval(t) for t in range(t0,tf)],\
	     [agent.inputs.xi(t)[0] for t in range(t0,tf)],\
	     [agent.inputs.xi(t)[1] for t in range(t0,tf)],\
	     [agent.inputs.xi(t)[2] for t in range(t0,tf)]]

	labels = ['initTime','PAbelief','PAoutcomeEval','xi1','xi2','xi3']

	N = 3	#number of bands

	print 'plotting agent inputs...'

	plot = Horizon().run(x,y,labels,\
	                     figname='agent '+str(agent.state.name)+' inputs',\
	                     bands=N)
	plot.subplots_adjust(left=0.07, right=0.998, top=0.99,bottom=0.01)
