
t = 5	#time of interest in simulation timesteps (set in settings)

#setup log file for this script
import logging
from behaviorSim.__util.setupLog import setupLog
setupLog()

import behaviorSim.API as API 

# === === === === === === AGENT SETUP === === === === === ===
sim   = API.getDefaultSimulation()

#API.congfigureSimulation(sim,script)

myAgent = API.getDefaultAgent(sim.environment)	#load default agent

#TODO: defaultAgent.tag = 'my very first agent'

# you can not reference the agent using 'myAgent' or 'environment.agent[0]'

# add agent to environment 



print ' === === === === === === SETTINGS === === === === === ==='
print '* simulation start time (sim-time): ' + str(sim.settings.simStartTime)
print '*     size of time step, deltaTime: ' + str(sim.settings.deltaTime)



print '\n === === === === === === INPUTS === === === === === ==='
# === to get data: ===
#<agentName>.inputs.<desiredValue>(<desiredTime>)
print '*   time(t): ' + str(sim.environment.agents[0].inputs.time(t))
# don't worry about if the data is 'there' or up-to-date; all of that is handled automagically, just ask for time you want

# === to get all data at one time (as a dict) === :
#<agentName>.inputs(<desiredTime>)
print '* inputs(3): ' + str(sim.environment.agents[0].inputs(3))
# that way you can explore available data in the object

# to get at more underlying raw data and methods use:
# help(sim.environment.agents[0].inputs)
# or
# print dir(sim.environment.agents[0].inputs)
# or explore the contents of inputs.inputs.py directly



print '\n === === === === === === STATE === === === === === ==='
# === to get data ===
#<agentName>.state.<desiredValue>(<desiredTime>)
print '*     agent name: '+str(sim.environment.agents[0].state.name)
print '* agent birthday: '+str(sim.environment.agents[0].state.birthday)
print '*   agent age(0): '+str(sim.environment.agents[0].state.age(0))
print '*   agent age(t): '+str(sim.environment.agents[0].state.age(t))

# === to explore available data in the object use ===
# help(environment.agents[0].state)
# or
# print dir(environment.agents[0].state)
# or explore the contents of state.state.py directly

#TODO: group these into PECS parts like this:
#agent.state(t)
#agent.state.P(t)
#agent.state.P.bodyTemp(t)



print '\n === === === === === === MOTIVES === === === === === ==='
print '* mortality: '+str(sim.environment.agents[0].motive.mortality(t))
#agent.motive.desire_PA(t)

#agent.motive(t)
#agent.motive.hunger(t)	# == agent.motive.drive_eat(t)
#agent.motive.sleepiness(t)



print '\n === === === === === === BEHAVIOR === === === === === ==='
print '*   behaviorKey: '+str(sim.environment.agents[0].behavior.behaviorKey(t))
print '* behaviorValue: '+str(sim.environment.agents[0].behavior.behaviorValue(t))
#agent.output(t)

#NOTE: all model.run() and all that is done automatically, just don't worry about it.

print '\n === === === === === === PLOTS === === === === === ==='
print 'plotAll? (y/n)'
choice = raw_input()
while choice != 'n' and choice != 'y':
	print choice + '? please enter y or n.'
	choice = raw_input()
if choice == 'y':
	print 'plottings all attributes for time 0 to 100'
	from behaviorSim.PECSplotter.plot import plotAll
	plotAll(sim.environment.agents[0],0,100)
	import pylab
	pylab.show()	

print 'show infoFlow? (y/n)'
choice = raw_input()
while choice != 'n' and choice != 'y':
	print choice + '? please enter y or n.'
	choice = raw_input()
if choice == 'y':
	import behaviorSim.PECSplotter.infoFlow as infoFlow
	infoFlow.showInfoFlow(sim.environment.agents[0])

# === === === === === === CUSTOMIZING THE AGENT === === === === === ===
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

