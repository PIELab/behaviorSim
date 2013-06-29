# this sample script recreates the results shown in Figure 9 of:
	# J.-Emeterio Navarro-Barrientos , Daniel E. Rivera & Linda M. Collins (2011):
	# A dynamical model for describing behavioural interventions for weight loss and body composition
	# change, Mathematical and Computer Modelling of Dynamical Systems: Methods, Tools and
	# Applications in Engineering and Related Sciences, 17:2, 183-203
# link: http://dx.doi.org/10.1080/13873954.2010.520409

from datetime import datetime, timedelta

print ' === === === === === === SETTINGS === === === === === ==='
# load settings (same as in _example_basicUsage)
from src.PECSagent.settings import settings
# customize settings
settings.deltaTime    = timedelta(days=1)
settings.simStartTime = datetime(2011, 1, 1, 12, 0, 0, 0)

print '* simulation start time (sim-time): ' + str(settings.simStartTime)
print '*     size of time step, deltaTime: ' + str(settings.deltaTime)

t0 = 0		#startTime
tf = 180	#endTime

# === === === === === === AGENT SETUP === === === === === ===
from src.environment.environment import environment
envmt = environment()	# load default environment

from src.PECSagent.agent import agent
agent1 = agent(envmt)	# load default agent

# customize the CSEL input functions (exogeneous flow vars)
from src.PECSagent.inputs.CSEL.attitudes import stepOne

def eatingAttitude(data,t):
	beforeChange = 7
	afterChange = 10
	changeT     = 10
	allOthers   = 1
	return stepOne(data,t,allOthers,'behavioralBelief',changeT,beforeChange,afterChange)
# TODO: agent1.inputs.attitudeChange_eatingGetter = eatingAttitude	#overwrite the default function

def exerciseAttitude(data,t):
# stepOne(data,t,value,steppedName,stepTime,beforeStep,afterStep):
	beforeChange = 1
	afterChange = 3
	changeT     = 30
	allOthers   = 1
	return stepOne(data,t,allOthers,'behavioralBelief',changeT,beforeChange,afterChange)
#agent1.inputs.attitudeChange_PAGetter = exerciseAttitude	#overwrite the default function
# TODO: this doesn't work...

print '\n === === === === === === INPUTS === === === === === ==='
print '      === CSEL inputs ==='
print '         (exogeneous flow determinants)'
print '* attitudeChange_PA: '+str(agent1.inputs.attitudeChange_PA(tf))
print '         (exogeneous flow vars:)'
print '* xi(t): '+str(agent1.inputs.xi(tf))

print '\n === === === === === === STATE === === === === === ==='
print '      === CSEL vars ==='
print '       (model constants)'
print '*    theta: '+str(agent1.state.agentPersonality.theta)
print '*      tau: '+str(agent1.state.agentPersonality.tau)
print '*    gamma: \n'+str(agent1.state.agentPersonality.gamma)
print '*     beta: \n'+str(agent1.state.agentPersonality.beta)
print '*     tauA: '+str(agent1.state.agentPersonality.tauA)
print '*    sigma: '+str(agent1.state.agentPersonality.sigma)
print '*      (disturbances)'
print '*  zeta(t): '+str(agent1.state.zeta(tf))
print '*      (state vars (endogeneous flow vars))'
print '*   eta(t): '+str(agent1.state.eta(tf))

import pylab
# this code aims to reproduce the plots from the paper
showTime = [agent1.inputs.time(t) for t in range(t0,tf)]
for etaNum in range(0,4):
	pylab.figure('eta'+str(etaNum))
	pylab.plot(showTime,[agent1.state.eta(t)[etaNum] for t in range(t0,tf)])
	pylab.draw()
pylab.show()

print 'show all plots? (y/n)'
choice = raw_input()
while choice != 'n' and choice != 'y':
	print choice + '? please enter y or n.'
	choice = raw_input()
if choice == 'y':
	from src.PECSplotter.plot import plotAll
	plotAll(agent1,0,100)
	import pylab
	pylab.show()



#EVERYTHING BELOW HERE ISN'T REALLY APPLICABLE (though perhaps the weight model can be incorporated)
print '\n === === === === === === MOTIVES === === === === === ==='
print str(agent1.motive(t))
#agent.motive.hunger(t)	# == agent.motive.drive_eat(t)
#agent.motive.desire_PA(t)
#agent.motive.sleepiness(t)


print '\n === === === === === === behavior === === === === === ==='
print str(agent1.behavior(t))


