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
	Encapsulates the environment and includes simulation
	   settings external to the environment.
	"""
	
	def __init__(self):
		self.settings    = settings()
		self.environment = environment()
		
	def run(t0, tf):
		"""
		Computes simulation values for t0 through tf.
		"""
		raise(NotImplementedError())