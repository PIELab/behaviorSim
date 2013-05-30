
t = 2	#time of interest

#agent set-up
import PECSagent.agent
agent1 = PECSagent.agent.agent()

# === to get data: ===
print 'initTime(2): ' + str(agent1.inputs.initTime(2))
# don't worry about if the data is 'there' or up-to-date; all of that is handled automagically, just ask for time you want

# === to get all data at once (as a dict) === :
print '     inputs: ' + str(agent1.inputs)
print '  inputs(0): ' + str(agent1.inputs(1))


# === how the raw data is handled (don't do this) ===
# attempted direct access shows data in memory (don't do this)
print '   initTime: ' + str(agent1.inputs._inputs__initTime)
# function call ensures that value is present and up-to-date (this is what you should be using)
print 'initTime(t): '  + str(agent1.inputs.initTime(t))
# and updates the raw data (as shown) (do not do this)
print '   initTime: ' + str(agent1.inputs._inputs__initTime)

#agent.state(t)
#agent.state.P(t)
#agent.state.P.bodyTemp(t)

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


