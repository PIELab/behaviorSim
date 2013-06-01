
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



print '\n === === === === === === MOTIVATIONS === === === === === ==='
print '* mortality: '+str(agent1.motivation.mortality(t))
#agent.motivation.desire_PA(t)

#agent.motivation(t)
#agent.motivation.hunger(t)	# == agent.motivation.drive_eat(t)
#agent.motivation.sleepiness(t)



print '\n === === === === === === OUTPUT === === === === === ==='
#agent.output(t)

#NOTE: all model.run() and all that is done automatically, just don't worry about it.


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

