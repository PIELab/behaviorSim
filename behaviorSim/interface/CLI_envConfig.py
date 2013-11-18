# -*- coding: utf-8 -*-
"""
Console configuration utility for behaviorSim environment.
"""

#import logging
#from behaviorSim.__util.setupLog import setupLog
#setupLog()

from behaviorSim.globals import ENVIRONMENT_CONFIG_SCRIPTS_PATH
from behaviorSim.interface.CLI import getUserInput,printFilesInDir


def finish():
	return

def selectNewConfig():
	print 'choose a new environment config file:'
	prompt,options = printFilesInDir(ENVIRONMENT_CONFIG_SCRIPTS_PATH)
	return 
	
def editConfig():
	print 'opening text editor (not implemented)'
	#TODO: do it!
	return
	
def configure(environemnt):
	"""call this to configure environment"""
	choices = {1 : finish,
	           2 : selectNewConfig,
	           3 : editConfig}
	prompt = """what would you like to do?
	\t 1) continue to console.
	\t 2) select new environment config file.
	\t 3) edit current config script"""
	
	choice = getUserInput(choices,prompt)
	print 'you choose:', choice
	print 'user configuration complete.'
