"""
The agent module defines the default agent setup. 
"""

from inputs.inputs     import inputs
from state.state       import state
from motive.motive     import motive
from behavior.behavior import behavior

class agent:
#	def __init__(self):
#		print 'WARN: agent is not in an environment!'
#		self.inputs   = inputs()
#		self.state    = state(self.inputs)
#		self.motive   = motive(self.state)
#		self.behavior = behavior(self.inputs,self.state,self.motive)

	def __init__(self,env):
		self.environment = env
		env.addAgent(self)

		self.inputs   = inputs(self.environment)
		self.state    = state(self.inputs)
		self.motive   = motive(self.state)
		self.behavior = behavior(self.inputs,self.state,self.motive)

	def __call__(self,t):
		"""
		Returns all data for the agent at given time t
		"""
		self.environment(t)
		self.inputs(t)
		self.state(t)
		self.behavior(t)
		return self.__dict__
