# -*- coding: utf-8 -*-
"""
Console simulation exploration activity.

Created on Sat Nov 23 12:17:57 2013

@author: tylar
"""
from behaviorSim.globals import SIMULATION_EXPLORATION_SCRIPTS_PATH
from behaviorSim.interface.CLI import getUserInput,printFilesInDir
import behaviorSim.API as API

class CLI_explore(object):
	
	def __init__(self):
		self.selectedScript=SIMULATION_EXPLORATION_SCRIPTS_PATH+'_default_.py'
	
	def explore(self,sim):
		"""call this to explore the given simulation"""
		print 'currently selected script:',self.selectedScript
		choice = self.explore
		while(choice != None):
			choices = {1 : None,
					2 : self.selectNewExploration,
			           3 : self.editExploration}
			prompt = """what would you like to do?
			\t 1) continue
			\t 2) select new exploration script file.
			\t 3) edit current exploration script"""
			
			choice = getUserInput(choices,prompt)
			try:
				choice(sim)
			except TypeError as e:
				if e.message=="'NoneType' object is not callable":
					self.finish(sim)
					return
				else: raise
				
	# === PRIVATE METHODS ===
	def finish(self,sim):
		"""runs the selected exploration script"""
		API.exploreSimulation(sim,self.selectedScript)
	
	def selectNewExploration(self,sim):
		print 'choose a new exploration script:'
		prompt,options = printFilesInDir(SIMULATION_EXPLORATION_SCRIPTS_PATH)
		choice = getUserInput(options,prompt)
		print choice, 'selected.'
		return 
		
	def editExploration(self,sim):
		print 'opening text editor (not implemented)'
		#TODO: do it!
		return