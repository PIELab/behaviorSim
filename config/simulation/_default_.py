# -*- coding: utf-8 -*-
"""
Loads the default configuration for the simulation.

Created on Sat Nov 23 09:11:05 2013

@author: tylar
"""

from behaviorSim.PECSagent.settings import settings
from behaviorSim.environment.environment import environment
from behaviorSim.PECSagent.agent import agent

def configure(sim):
	sim.settings = settings()
	sim.environment = environment()
	agent(sim.environment)