# this file defines a set of functions for plotting the various attributes of a PECS agent

import pylab

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

#plots all motives of the agent as time series from t0 to tf
def plotMotive(agent,t0,tf):
	print 'loading agent motive...'
	time =     [agent.inputs.time(t) for t in range(t0,tf)]

	mortality =  [agent.motive.mortality(t) for t in range(t0,tf)]
	will_PA =  [agent.motive.will_PA(t) for t in range(t0,tf)]
	
	print 'plotting agent motive...'

	pylab.figure('agent '+str(agent.state.name)+' motive')

	pylab.subplot(2,1,1)
	pylab.plot(time,mortality)
	pylab.ylabel('mortality')

	pylab.subplot(2,1,2)
	pylab.plot(time,will_PA)
	pylab.ylabel('will_PA')


# plots all state of the agent as a time series from t0 to tf
def plotState(agent,t0,tf): 
	print 'loading agent state...'
	time =     [agent.inputs.time(t) for t in range(t0,tf)]

	age =     [agent.state.age(t).total_seconds()/(60*60*24*365.242) for t in range(t0,tf)]
	zeta1 =     [agent.state.zeta(t)[0] for t in range(t0,tf)]
	zeta2 =     [agent.state.zeta(t)[1] for t in range(t0,tf)]
	zeta3 =     [agent.state.zeta(t)[2] for t in range(t0,tf)]
	zeta4 =     [agent.state.zeta(t)[3] for t in range(t0,tf)]
	zeta5 =     [agent.state.zeta(t)[4] for t in range(t0,tf)]
	eta1 =     [agent.state.eta(t)[0] for t in range(t0,tf)]
	eta2 =     [agent.state.eta(t)[1] for t in range(t0,tf)]
	eta3 =     [agent.state.eta(t)[2] for t in range(t0,tf)]
	eta4 =     [agent.state.eta(t)[3] for t in range(t0,tf)]
	eta5 =     [agent.state.eta(t)[4] for t in range(t0,tf)]

	print 'plotting agent state...'

	pylab.figure('agent '+str(agent.state.name)+' state')

	pylab.subplot(3,5,1)
	pylab.plot(time,age)
	pylab.ylabel('age')
	# force yticks to be in years (and not deci-years):
	locs,labels = pylab.yticks()
	pylab.yticks(locs, map(lambda ageArray: "%g" % ageArray, locs))
	
	#subplots 2-5 empty

	#zeta on plots 6-10
	pylab.subplot(3,5,6)
	pylab.plot(time,zeta1)
	pylab.ylabel('zeta1')
	pylab.subplot(3,5,7)
	pylab.plot(time,zeta2)
	pylab.ylabel('zeta2')
	pylab.subplot(3,5,8)
	pylab.plot(time,zeta3)
	pylab.ylabel('zeta3')
	pylab.subplot(3,5,9)
	pylab.plot(time,zeta4)
	pylab.ylabel('zeta4')
	pylab.subplot(3,5,10)
	pylab.plot(time,zeta5)
	pylab.ylabel('zeta5')

	#eta on plots 11-15
	pylab.subplot(3,5,11)
	pylab.plot(time,eta1)
	pylab.ylabel('eta1')
	pylab.subplot(3,5,12)
	pylab.plot(time,eta2)
	pylab.ylabel('eta2')
	pylab.subplot(3,5,13)
	pylab.plot(time,eta3)
	pylab.ylabel('eta3')
	pylab.subplot(3,5,14)
	pylab.plot(time,eta4)
	pylab.ylabel('eta4')
	pylab.subplot(3,5,15)
	pylab.plot(time,eta5)
	pylab.ylabel('eta5')


# plots all inputs of the agent as a time series from t0 to tf
def plotInputs(agent,t0,tf): 
	print 'loading agent inputs...'
	time =     [agent.inputs.time(t) for t in range(t0,tf)]

	initTime = [agent.inputs.initTime(t) for t in range(t0,tf)]
	PAbelief = [agent.inputs.PAbelief(t) for t in range(t0,tf)]
	PAoutcome = [agent.inputs.PAoutcomeEval(t) for t in range(t0,tf)]
	xi1 = [agent.inputs.xi(t)[0] for t in range(t0,tf)]
	xi2 = [agent.inputs.xi(t)[1] for t in range(t0,tf)]
	xi3 = [agent.inputs.xi(t)[2] for t in range(t0,tf)]

	print 'plotting agent inputs...'

	pylab.figure('agent '+str(agent.state.name)+' inputs')

	pylab.subplot(611)
	pylab.plot(time,initTime)
	pylab.ylabel('initTime')

	pylab.subplot(612)
	pylab.plot(time,PAbelief)
	pylab.ylabel('PAbelief')

	pylab.subplot(613)
	pylab.plot(time,PAoutcome)
	pylab.ylabel('PAoutcomeEval')

	pylab.subplot(614)
	pylab.plot(time,xi1)
	pylab.ylabel('xi1')

	pylab.subplot(615)
	pylab.plot(time,xi2)
	pylab.ylabel('xi2')

	pylab.subplot(616)
	pylab.plot(time,xi3)
	pylab.ylabel('xi3')	
