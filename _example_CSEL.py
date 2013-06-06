
t = 5	#time of interest in simulation timesteps (set in settings)

# === === === === === === AGENT SETUP === === === === === ===
import PECSagent.agent
agent1 = PECSagent.agent.agent()



print ' === === === === === === SETTINGS === === === === === ==='
# load settings (same as in _example_basicUsage)
from PECSagent.settings import settings
print '* simulation start time (sim-time): ' + str(settings.simStartTime)
print '*     size of time step, deltaTime: ' + str(settings.deltaTime)


print '\n === === === === === === INPUTS === === === === === ==='
# === to get data: === (same as in _example_basicUsage)
print '*   time(t): ' + str(agent1.inputs.time(t))
# or print '* inputs(3): ' + str(agent1.inputs(3))
print '      === CSEL inputs ==='
print '         (exogeneous flow determinants)'
print '*      PAbelief(t): '+str(agent1.inputs.PAbelief(t))
print '* PAoutcomeEval(t): '+str(agent1.inputs.PAoutcomeEval(t))
print '         (exogeneous flow vars:)'
print '*            xi(t): '+str(agent1.inputs.xi(t))

print '\n === === === === === === STATE === === === === === ==='
# === to get data === 
#<agentName>.state.<desiredValue>(<desiredTime>)
print '*     agent name: '+agent1.state.name
print '*   agent age(t): '+str(agent1.state.age(t))
print '      === CSEL vars ==='
print '       (model constants)'
print '*    theta: '+str(agent1.state.theta)
print '*      tau: '+str(agent1.state.tau)
print '*    gamma: \n'+str(agent1.state.gamma)
print '*     beta: \n'+str(agent1.state.beta)
print '*     tauA: '+str(agent1.state.tauA)
print '*    sigma: '+str(agent1.state.sigma)
print '*      (disturbances)'
print '*  zeta(t): '+str(agent1.state.zeta(t))
print '*      (state vars (endogeneous flow vars))'
print '*   eta(t): '+str(agent1.state.eta(t))

print 'plot your CSEL state vars? (y/n)'
choice = raw_input()
while choice != 'n' and choice != 'y':
	print choice + '? please enter y or n.'
	choice = raw_input()
if choice == 'y':
	import pylab
	showTime = [agent1.inputs.time(t) for t in range(0,10)]
	for etaNum in range(0,4):
		pylab.figure('eta'+str(etaNum))
		pylab.plot(showTime,[agent1.state.eta(t)[etaNum] for t in range(0,10)])
		pylab.draw()
	pylab.show()
#else choice == 'n', do nothing.

# === to explore available data in the object use ===
# help(agent1.state)
# or
# print dir(agent1.state)
# or explore the contents of state.state.py directly

#agent.state(t)
#agent.state.P(t)
#agent.state.P.bodyTemp(t)

print '\n === === === === === === MOTIVES === === === === === ==='
print str(agent1.motive(t))
#agent.motive.hunger(t)	# == agent.motive.drive_eat(t)
#agent.motive.desire_PA(t)
#agent.motive.sleepiness(t)


print '\n === === === === === === behavior === === === === === ==='
print str(agent1.behavior(t))

#NOTE: all model.run() and all that is done automatically, just don't worry about it.



#this is how I want to set the parts:
#agent.setX(relative.loc.of.file.or.something)
#agent.setFp(...
#agent.setFe(...
#...
#agent.setZp(...
#agent.setZe(...
#agent.setG(...
#agent.setH(...
#...

