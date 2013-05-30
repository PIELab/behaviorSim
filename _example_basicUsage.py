
t = 2	#time of interest

#agent set-up
import PECSagent.agent
agent1 = PECSagent.agent.agent()

# === === === === === === INPUT === === === === === ===
# === to get data: ===
#<agentName>.inputs.<desiredValue>(<desiredTime>)
print 'time(2): ' + str(agent1.inputs.time(2)) + agent1.inputs.timeUnits
# don't worry about if the data is 'there' or up-to-date; all of that is handled automagically, just ask for time you want

# === to get all data at one time (as a dict) === :
#<agentName>.inputs(<desiredTime>)
print '  inputs(0): ' + str(agent1.inputs(1))

# === to explore available data in the object use ===
# help(agent1.inputs)
# or
# print dir(agent1.inputs)
# or explore the contents of agent.inputs.py directly



# === === === === === === STATE === === === === === ===
#agent.state(t)
#agent.state.P(t)
#agent.state.P.bodyTemp(t)



# === === === === === === OUTPUT === === === === === ===
#agent.output(t)

#NOTE: all model.run() and all that crap is implicit and done automatically



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

