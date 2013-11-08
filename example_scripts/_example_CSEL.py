# this sample script recreates the results shown in Figure 9 of:
	# J.-Emeterio Navarro-Barrientos , Daniel E. Rivera & Linda M. Collins (2011):
	# A dynamical model for describing behavioural interventions for weight loss and body composition
	# change, Mathematical and Computer Modelling of Dynamical Systems: Methods, Tools and
	# Applications in Engineering and Related Sciences, 17:2, 183-203
# link: http://dx.doi.org/10.1080/13873954.2010.520409

from datetime import datetime, timedelta

#setup log file for this script
import logging
from behaviorSim.__util.setupLog import setupLog
setupLog()

print ' === === === === === === SETTINGS === === === === === ==='
# load settings (same as in _example_basicUsage)
from behaviorSim.PECSagent.settings import settings
# customize settings
settings.deltaTime    = timedelta(days=1)
settings.simStartTime = datetime(2011, 1, 1, 12, 0, 0, 0)

print '* simulation start time (sim-time): ' + str(settings.simStartTime)
print '*     size of time step, deltaTime: ' + str(settings.deltaTime)

t0 = 0   #startTime
tf = 180 #endTime

# === === === === === === AGENT SETUP === === === === === ===
from behaviorSim.environment.environment import environment
envmt = environment()	# load default environment

# load agents personalities for i, ii, and iii
from behaviorSim.PECSagent.agent import agent
from behaviorSim.PECSagent.state.CSEL import agent_i, agent_ii, agent_iii
agent1 = agent(envmt)
agent1.state.setPersonality(agent_i.personality())

agent2 = agent(envmt)
agent2.state.setPersonality(agent_ii.personality())

agent3 = agent(envmt)
agent3.state.setPersonality(agent_iii.personality())
#add disturbances
from behaviorSim.PECSagent.state.CSEL.model_ddeint_firstOrder_withDisturbances import getEta
# print 'args='+str(agent3.state.eta_PA.args)
#def getEta(data,t,xi_PA,agent,zeta_PA):
agent3.state.eta_PA.setFunction(getEta,agent3.inputs.xi_PA,agent3.state.personality,agent3.state.zeta_PA)
agent3.state.eta_EB.setFunction(getEta,agent3.inputs.xi_EB,agent3.state.personality,agent3.state.zeta_EB)

# customize the CSEL input functions (exogeneous flow vars)
from behaviorSim.PECSagent.inputs.CSEL.attitudes import stepOne

def eatingAttitude(t):
	beforeChange = 7
	afterChange = 10
	changeT     = 10
	allOthers   = 1
	return stepOne(t,allOthers,'behavioralBelief',changeT,beforeChange,afterChange)
agent1.inputs.attitudeChange_EB.setFunction(eatingAttitude)	#overwrite the default function
agent2.inputs.attitudeChange_EB.setFunction(eatingAttitude)	#overwrite the default function
agent3.inputs.attitudeChange_EB.setFunction(eatingAttitude)	#overwrite the default function

def exerciseAttitude(t):
# stepOne(data,t,value,steppedName,stepTime,beforeStep,afterStep):
	beforeChange = 1
	afterChange = 3
	changeT     = 30
	allOthers   = 1
	return stepOne(t,allOthers,'behavioralBelief',changeT,beforeChange,afterChange)
agent1.inputs.attitudeChange_PA.setFunction(exerciseAttitude)	#overwrite the default function
agent2.inputs.attitudeChange_PA.setFunction(exerciseAttitude)	#overwrite the default function
agent3.inputs.attitudeChange_PA.setFunction(exerciseAttitude)	#overwrite the default function

print '\n === === === === === === INPUTS === === === === === ==='
print '      === CSEL inputs ==='
print '         (exogeneous flow determinants)'
print '* attitudeChange_PA: '+str(agent1.inputs.attitudeChange_PA(tf))
print '         (exogeneous flow vars:)'
print '* xi_PA(t): '+str(agent1.inputs.xi_PA(tf))

print '\n === === === === === === STATE === === === === === ==='
print '      === CSEL vars ==='
print '       (model constants)'
print '*    theta: '+str(agent1.state.personality.theta)
print '*      tau: '+str(agent1.state.personality.tau)
print '*    gamma: \n'+str(agent1.state.personality.gamma)
print '*     beta: \n'+str(agent1.state.personality.beta)
print '*     tauA: '+str(agent1.state.personality.tauA)
print '*    sigma: '+str(agent1.state.personality.sigma)
print '*      (disturbances)'
print '*  zeta_PA(t): '+str(agent1.state.zeta_PA(tf))
print '*      (state vars (endogeneous flow vars))'
print '*   eta_PA(t): '+str(agent1.state.eta_PA(tf))
print '*   eta_EB(t): '+str(agent1.state.eta_EB(tf))

import pylab
#reduce font size of display
pylab.rcParams.update({'font.size': 8})

# this code aims to reproduce the plots from the paper
# showTime = [agent1.inputs.time(t) for t in range(t0,tf)]	#use this to show dates rather than indexes
showTime = range(t0,tf)
pylab.figure('CSEL behavior model plot')

# odd plots are Eating Behavior
pylab.subplot(421)
pylab.title('Energy Intake')
pylab.ylabel('behavioral beliefs')
pylab.plot(showTime,[agent1.inputs.attitudeChange_EB(t).behavioralBelief for t in range(t0,tf)])
pylab.plot(showTime,[agent2.inputs.attitudeChange_EB(t).behavioralBelief for t in range(t0,tf)])
pylab.plot(showTime,[agent3.inputs.attitudeChange_EB(t).behavioralBelief for t in range(t0,tf)])

pylab.subplot(423)
pylab.ylabel('attitude (eta1)')
pylab.plot(showTime,[agent1.state.eta_EB(t)[0] for t in range(t0,tf)])
pylab.plot(showTime,[agent2.state.eta_EB(t)[0] for t in range(t0,tf)])
pylab.plot(showTime,[agent3.state.eta_EB(t)[0] for t in range(t0,tf)])

pylab.subplot(425)
pylab.ylabel('intention (eta4)')
pylab.plot(showTime,[agent1.state.eta_EB(t)[3] for t in range(t0,tf)])
pylab.plot(showTime,[agent2.state.eta_EB(t)[3] for t in range(t0,tf)])
pylab.plot(showTime,[agent3.state.eta_EB(t)[3] for t in range(t0,tf)])

pylab.subplot(427)
pylab.ylabel('behavior (eta5)')
pylab.plot(showTime,[agent1.state.eta_EB(t)[4] for t in range(t0,tf)])
pylab.plot(showTime,[agent2.state.eta_EB(t)[4] for t in range(t0,tf)])
pylab.plot(showTime,[agent3.state.eta_EB(t)[4] for t in range(t0,tf)])

pylab.xlabel('time')

# even plots are PA
pylab.subplot(422)
pylab.title('Pysical activity')
pylab.ylabel('behavioral beliefs')
pylab.plot(showTime,[agent1.inputs.attitudeChange_PA(t).behavioralBelief for t in range(t0,tf)])
pylab.plot(showTime,[agent2.inputs.attitudeChange_PA(t).behavioralBelief for t in range(t0,tf)])
pylab.plot(showTime,[agent3.inputs.attitudeChange_PA(t).behavioralBelief for t in range(t0,tf)])

pylab.subplot(424)
pylab.ylabel('attitude (eta1)')
pylab.plot(showTime,[agent1.state.eta_PA(t)[0] for t in range(t0,tf)])
pylab.plot(showTime,[agent2.state.eta_PA(t)[0] for t in range(t0,tf)])
pylab.plot(showTime,[agent3.state.eta_PA(t)[0] for t in range(t0,tf)])

pylab.subplot(426)
pylab.ylabel('intention (eta4)')
pylab.plot(showTime,[agent1.state.eta_PA(t)[3] for t in range(t0,tf)])
pylab.plot(showTime,[agent2.state.eta_PA(t)[3] for t in range(t0,tf)])
pylab.plot(showTime,[agent3.state.eta_PA(t)[3] for t in range(t0,tf)])

pylab.subplot(428)
pylab.ylabel('behavior (eta5)')
pylab.plot(showTime,[agent1.state.eta_PA(t)[4] for t in range(t0,tf)])
pylab.plot(showTime,[agent2.state.eta_PA(t)[4] for t in range(t0,tf)])
pylab.plot(showTime,[agent3.state.eta_PA(t)[4] for t in range(t0,tf)])

pylab.xlabel('time')

pylab.draw()
pylab.show()

def ask(question):
	print question+' (y/n)'
	choice = raw_input()
	while choice != 'n' and choice != 'y':
		print choice + '? please enter y or n.'
		choice = raw_input()
	return choice


if ask('plot all?') == 'y':
	from behaviorSim.PECSplotter.plot import plotAll
	plotAll(agent1,t0,tf)
	import pylab
	pylab.show()

if ask('show infoFlow?') == 'y':
	from behaviorSim.PECSplotter.infoFlow import showInfoFlow
	print 'showing agent 1 infoFlow...'
	showInfoFlow(agent1)
	


#EVERYTHING BELOW HERE ISN'T REALLY APPLICABLE (though perhaps the weight model can be incorporated)
print '\n === === === === === === MOTIVES === === === === === ==='
print str(agent1.motive(t))
#agent.motive.hunger(t)	# == agent.motive.drive_eat(t)
#agent.motive.desire_PA(t)
#agent.motive.sleepiness(t)


print '\n === === === === === === behavior === === === === === ==='
print str(agent1.behavior(t))


