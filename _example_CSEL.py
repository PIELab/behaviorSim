# this sample script recreates the results shown in Figure 9 of:
	# J.-Emeterio Navarro-Barrientos , Daniel E. Rivera & Linda M. Collins (2011):
	# A dynamical model for describing behavioural interventions for weight loss and body composition
	# change, Mathematical and Computer Modelling of Dynamical Systems: Methods, Tools and
	# Applications in Engineering and Related Sciences, 17:2, 183-203
# link: http://dx.doi.org/10.1080/13873954.2010.520409

from datetime import datetime, timedelta

#setup log file for this script
import logging
print str(logging.getLogger())
logging.basicConfig(filename='src/__logs/CSELexample.log',\
	                 level=logging.DEBUG,\
	                format='%(asctime)s %(levelname)s:%(message)s',\
                   filemode='w')

print ' === === === === === === SETTINGS === === === === === ==='
# load settings (same as in _example_basicUsage)
from src.PECSagent.settings import settings
# customize settings
settings.deltaTime    = timedelta(days=1)
settings.simStartTime = datetime(2011, 1, 1, 12, 0, 0, 0)

print '* simulation start time (sim-time): ' + str(settings.simStartTime)
print '*     size of time step, deltaTime: ' + str(settings.deltaTime)

t0 = 0		#startTime
tf = 50	#endTime

# === === === === === === AGENT SETUP === === === === === ===
from src.environment.environment import environment
envmt = environment()	# load default environment

from src.PECSagent.agent import agent
agent1 = agent(envmt)	# load default agent

# customize the CSEL input functions (exogeneous flow vars)
from src.PECSagent.inputs.CSEL.attitudes import stepOne

def eatingAttitude(t):
	beforeChange = 7
	afterChange = 10
	changeT     = 10
	allOthers   = 1
	return stepOne(t,allOthers,'behavioralBelief',changeT,beforeChange,afterChange)
# TODO: agent1.inputs.attitudeChange_eatingGetter = eatingAttitude	#overwrite the default function

def exerciseAttitude(t):
# stepOne(data,t,value,steppedName,stepTime,beforeStep,afterStep):
	beforeChange = 1
	afterChange = 3
	changeT     = 30
	allOthers   = 1
	return stepOne(t,allOthers,'behavioralBelief',changeT,beforeChange,afterChange)
agent1.inputs.attitudeChange_PA.setFunction(exerciseAttitude)	#overwrite the default function

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
#reduce font size of display
pylab.rcParams.update({'font.size': 8})

# this code aims to reproduce the plots from the paper
# showTime = [agent1.inputs.time(t) for t in range(t0,tf)]	#use this to show dates rather than indexes
showTime = range(t0,tf)
pylab.figure('CSEL behavior model plot')

# odd plots are Energy intake
pylab.subplot(421)
pylab.title('Energy Intake')
pylab.ylabel('behavioral beliefs')

pylab.subplot(423)
pylab.ylabel('attitude (eta1)')

pylab.subplot(425)
pylab.ylabel('intention (eta4)')

pylab.subplot(427)
pylab.ylabel('behavior (eta5)')
pylab.xlabel('time')

# even plots are PA
pylab.subplot(422)
pylab.title('Pysical activity')
pylab.plot(showTime,[agent1.inputs.attitudeChange_PA(t).behavioralBelief for t in range(t0,tf)])

pylab.subplot(424)
pylab.ylabel('attitude (eta1)')
pylab.plot(showTime,[agent1.state.eta(t)[0] for t in range(t0,tf)])

pylab.subplot(426)
pylab.ylabel('intention (eta4)')
pylab.plot(showTime,[agent1.state.eta(t)[3] for t in range(t0,tf)])

pylab.subplot(428)
pylab.ylabel('behavior (eta5)')
pylab.plot(showTime,[agent1.state.eta(t)[4] for t in range(t0,tf)])

pylab.xlabel('time')

pylab.draw()
pylab.show()

print 'show all plots? (y/n)'
choice = raw_input()
while choice != 'n' and choice != 'y':
	print choice + '? please enter y or n.'
	choice = raw_input()
if choice == 'y':
	from src.PECSplotter.plot import plotAll
	plotAll(agent1,t0,tf)
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


