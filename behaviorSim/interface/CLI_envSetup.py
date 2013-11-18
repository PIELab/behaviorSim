"""
Console interface for setting up a simulation.
"""

#import logging
#from behaviorSim.__util.setupLog import setupLog
#setupLog()

from behaviorSim.environment.environment import environment
from behaviorSim.PECSagent.agent import agent

class setup(environment):
	"""
	This class adds a CLI interface to the environment settings.
	"""
	def __init__(self):
		print 'setting up default environment...'
		super(self.__class__,self).__init__()
		print 'environment setup complete.'
		self.showEnvStatus()
		self.listAgents()
	
	def showEnvStatus(self):
		"""
		Shows what the current environment is like.
		"""
		print 'current environment:',self.name
		print '# agents in sim:',str(len(self.agents))
		print 'additional values available:',self.__dict__.keys()
		#TODO: could use pprint here
		
	def listAgents(self):
		"""
		Lists all agents in current environment
		"""
		print 'agents in environment "',self.name,'":'
		print [a.state.name for a in self.agents]
	
	def setupAgent(self):
		print 'setting up default agent...'
		self.addAgent(agent(self))	#add a default agent
		print 'done'
