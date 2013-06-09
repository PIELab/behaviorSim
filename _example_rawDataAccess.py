from src.environment.environment import environment
envmt = environment()	#load default environment

from src.PECSagent.agent import agent
agent1 = agent(envmt)	#load default agent

t = 3

# === how the raw data is handled (don't do this) ===

# attempted direct access shows data in memory (don't do this)
print '   initTime: ' + str(agent1.inputs._inputs__initTime)
# note that it is empty, something likke _inputs__initTime[t] here would cause out-of-bounds exception

# function call ensures that value is present and up-to-date (this is what you should be using)
print 'initTime(t): '  + str(agent1.inputs.initTime(t))

# and updates the raw data (as shown) (do not do this)
print '   initTime: ' + str(agent1.inputs._inputs__initTime)
