
t = 5	#time of interest in simulation timesteps (set in settings)

#setup log file for this script
import logging
from behaviorSim.__util.setupLog import setupLog
setupLog()

# === === === === === === AGENT SETUP === === === === === ===
from behaviorSim.environment.environment import environment
envmt = environment()	#load default environment

from behaviorSim.PECSagent.agent import agent
myAgent = agent(envmt)	#load default agent
#TODO: customize the agent
#TODO: defaultAgent.tag = 'my very first agent'

# you can not reference the agent using 'myAgent' or 'envmt.agent[0]'

# add agent to environment 



print ' === === === === === === SETTINGS === === === === === ==='
# load settings of the simulation (just FYI here)
from behaviorSim.PECSagent.settings import settings
print '* simulation start time (sim-time): ' + str(settings.simStartTime)
print '*     size of time step, deltaTime: ' + str(settings.deltaTime)

print ' === === === === === === DATA === === === === === ==='
print envmt.agents[0].inputs(0)
print envmt.agents[0].state(0)
print envmt.agents[0].motive(0)
print envmt.agents[0].behavior(0)

print ' === === === === === === infoFlow === === === === === ==='
# show agent infoFlow diagram
import behaviorSim.PECSplotter.infoFlow as infoFlow
infoFlow.showInfoFlow(envmt.agents[0])

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

