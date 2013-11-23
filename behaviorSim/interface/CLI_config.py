# -*- coding: utf-8 -*-
"""
Console configuration utility for behaviorSim environment.
"""

#import logging
#from behaviorSim.__util.setupLog import setupLog
#setupLog()

from behaviorSim.globals import SIMULATION_CONFIG_SCRIPTS_PATH
from behaviorSim.interface.CLI import getUserInput,printFilesInDir

from behaviorSim.PECSagent.agent import agent

import  behaviorSim.API as API

class CLI_config(object):
	
	def __init__(self):
		self.configured = False # flag to show if a setup has been run yet.
	
	def configure(self,sim):
		"""call this to configure environment"""
		
		# run default setup
		defaultConfigFile = SIMULATION_CONFIG_SCRIPTS_PATH+'_default_.py'
		API.configureSimulation(sim,defaultConfigFile)

		self.showAll(sim)
		
		# give user other setup options
		choice = self.configure
		while(choice != None):
			choices = {1 : None,
					2 : self.showEnvStatus,
			           3 : self.selectNewConfig,
			           4 : self.editConfig}
			prompt = """what would you like to do?
			\t 1) continue
			\t 2) show environment details
			\t 3) select new simulation config file.
			\t 4) edit current simulation config script"""
			
			choice = getUserInput(choices,prompt)
			try:
				choice(sim)
			except TypeError as e:
				if e.message=="'NoneType' object is not callable":
					self.finish()
					return
				else: raise
				
	# === PRIVATE METHODS ===
	
	def showSettings(self,sim):
		print 'simulation settings:'
		print sim.settings.__dict__
	
	def showEnvStatus(self,sim):
		"""
		Shows what the current environment is like.
		"""
		print 'current environment:',sim.environment.name
		print '# agents in sim:',str(len(sim.environment.agents))
		print 'additional values available:',sim.environment.__dict__.keys()
		#TODO: could use pprint here
		
	def listAgents(self,sim):
		"""
		Lists all agents in current environment
		"""
		print 'agents in environment "',sim.environment.name,'":'
		print [a.state.name for a in sim.environment.agents]
	
	def setupAgent(self,sim):
		print 'setting up default agent...'
		sim.environment.addAgent(agent(sim.environment))	#add a default agent
		print 'done'
	
	def finish(self):
		print 'user configuration complete.'
		return
	
	def selectNewConfig(self,sim):
		print 'choose a new environment config file:'
		prompt,options = printFilesInDir(SIMULATION_CONFIG_SCRIPTS_PATH)
		choice = getUserInput(options,prompt)
		print 'you choose:',choice
		print 'running config script...'
		API.configureSimulation(sim,choice)
		self.configured = True
		print 'done.'
		self.showAll(sim)
		return 
		
	def showAll(self,sim):
		"""shows all available info"""
		self.showEnvStatus(sim)
		self.showSettings(sim)
		
	def editConfig(self,sim):
		print 'opening text editor (not implemented)'
		#TODO: do it!
		return
				