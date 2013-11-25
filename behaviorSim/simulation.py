# -*- coding: utf-8 -*-
"""
Defines simulation class.

Created on Mon Nov 18 17:27:52 2013

@author: tylar
"""

from behaviorSim.PECSagent.settings import settings
from behaviorSim.environment.environment import environment

class simulation(object):
	"""
		The simulation object encapsulates the environment and includes 
simulation settings external to the environment.

public attributes:
	settings = simulation settings
	environment = environment object including simulation agents
		
To get a closer look at settings or environment, try:
	>> help(behaviorSim.settings)
	for information on simulation settings
	
	>> help(behaviorSim.environment)
	for information on the environment and agents
	
	>> help(behaviorSim.environment.agent[0])
	for information about a particular agent
	"""
	
	def __init__(self):
		self.settings    = settings()
		self.environment = environment()
		
	def run(t0, tf):
		"""
		Computes simulation values for t0 through tf.
		"""
		raise(NotImplementedError())