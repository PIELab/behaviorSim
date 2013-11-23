# -*- coding: utf-8 -*-
"""
This file defines the API for the behaviorSim toolkit

Created on Tue Nov 19 22:04:44 2013

@author: tylar
"""

import imp

def getDefaultSimulation():
	import behaviorSim.simulation
	return behaviorSim.simulation.simulation()
	
def configureSimulation(sim,configScript):
	imp.load_source('configuration',configScript).configure(sim)
	
def exploreSimulation(sim,exploreScript):
	imp.load_source('exploration',exploreScript).explore(sim)
	
def getDefaultEnvironment():
	from behaviorSim.environment.environment import environment
	return environment()
	
def getDefaultAgent(envmt):
	from behaviorSim.PECSagent.agent import agent
	return agent(envmt)


