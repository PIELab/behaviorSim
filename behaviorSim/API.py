# -*- coding: utf-8 -*-
"""
This file defines the API for the behaviorSim toolkit

Created on Tue Nov 19 22:04:44 2013

@author: tylar
"""

import imp

from behaviorSim.__util.agentData import dataObject

### OBJECT CREATION ###
def getDefaultSimulation():
	''' returns a new simulation with the default configuration '''
	import behaviorSim.simulation
	return behaviorSim.simulation.simulation()
	
	''' returns a new environment with the default configuration '''
def getDefaultEnvironment():
	from behaviorSim.environment.environment import environment
	return environment()
	
	''' returns a new agent with the default configuration '''
def getDefaultAgent(envmt):
	from behaviorSim.PECSagent.agent import agent
	return agent(envmt)
	
### SCRIPTED OBJECT CONFIGURATION ###
def configureSimulation(sim,configScript):
	''' configures the given simulation using the given config script'''
	imp.load_source('configuration',configScript).configure(sim)
	
### SCRIPTED OBJECT EXPLORATION ###
	''' runs the given exploration script for the given simulation '''
def exploreSimulation(sim,exploreScript):
	imp.load_source('exploration_sim',exploreScript).explore(sim)
	
	''' runs the given exploration script for the given agent '''
def exploreAgent(agent,exploreScript):
	imp.load_source('exploration_agent',exploreScript).explore(agent)

### DETAILED OBJECT CUSTOMIZATION ###

def removeConstruct(agentComponent,constructName):
	''' remove the specified data construct from the given agent'''
	print 'del attribute agent.'+str(constructName)		
	
	delattr(agentComponent, constructName)

def addConstruct(agentComponent,constructObj):
	''' add the given data construct to the given agent component '''
	setattr(agentComponent,constructObj.name,constructObj)
	
def getConstruct(constructName, contructCalcFunc, *constructDependencies):
	''' return a data construct using given information '''
	return dataObject(constructName,contructCalcFunc, constructDependencies)
	
#TODO: include detailed environment customization


	
