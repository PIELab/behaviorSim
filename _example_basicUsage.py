
t = 5	#time of interest in simulation timesteps (set in settings)

# === === === === === === AGENT SETUP === === === === === ===
import PECSagent.agent
agent1 = PECSagent.agent.agent()



print ' === === === === === === SETTINGS === === === === === ==='
# load settings of the simulation (just FYI here)
from PECSagent.settings import settings
print '* simulation start time (sim-time): ' + str(settings.simStartTime)
print '*     size of time step, deltaTime: ' + str(settings.deltaTime)



print '\n === === === === === === INPUTS === === === === === ==='
# === to get data: ===
#<agentName>.inputs.<desiredValue>(<desiredTime>)
print '*   time(t): ' + str(agent1.inputs.time(t))
# don't worry about if the data is 'there' or up-to-date; all of that is handled automagically, just ask for time you want

# === to get all data at one time (as a dict) === :
#<agentName>.inputs(<desiredTime>)
print '* inputs(3): ' + str(agent1.inputs(3))
# that way you can explore available data in the object

# to get at more underlying raw data and methods use:
# help(agent1.inputs)
# or
# print dir(agent1.inputs)
# or explore the contents of inputs.inputs.py directly



print '\n === === === === === === STATE === === === === === ==='
# === to get data ===
#<agentName>.state.<desiredValue>(<desiredTime>)
print '*     agent name: '+agent1.state.name
print '* agent birthday: '+str(agent1.state.birthday)
print '*   agent age(0): '+str(agent1.state.age(0))
print '*   agent age(t): '+str(agent1.state.age(t))

# === to explore available data in the object use ===
# help(agent1.state)
# or
# print dir(agent1.state)
# or explore the contents of state.state.py directly

#TODO: group these into PECS parts like this:
#agent.state(t)
#agent.state.P(t)
#agent.state.P.bodyTemp(t)



print '\n === === === === === === MOTIVES === === === === === ==='
print '* mortality: '+str(agent1.motive.mortality(t))
#agent.motive.desire_PA(t)

#agent.motive(t)
#agent.motive.hunger(t)	# == agent.motive.drive_eat(t)
#agent.motive.sleepiness(t)



print '\n === === === === === === BEHAVIOR === === === === === ==='
print '*   behaviorKey: '+str(agent1.behavior.behaviorKey(t))
print '* behaviorValue: '+str(agent1.behavior.behaviorValue(t))
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
	import PECSplotter.plot
	PECSplotter.plot.plotAll(agent1,0,100)
	import pylab
	pylab.show()	


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

