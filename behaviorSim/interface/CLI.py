"""
Defines a Command-Line Interface for choosing a script
"""

import glob	# for file listing
import os   # for path joining
import imp  # for importing file at a path
import code # for starting interactive mode

from behaviorSim.globals import *

def printFilesInDir(directory):
	"""
	creates sting with numbered list of all .py scripts in given directory (excluding __init__.py) and returns string and a dict which maps numbers to filenames.
	"""
	string = ''
	options = dict()
	for inputName in glob.glob(os.path.join(directory,'*.py')):
		if inputName == './example_scripts/__init__.py': continue

		entryNum = len(options)
		options[entryNum] = inputName

		string += '\t'+str(entryNum)+') '+options[entryNum]+'\n'
	return string,options

def getUserInput(options,prompt):
	"""
	Requests user input using given prompt until user makes a choice within options dict.
	"""
	if len(options) < 1:
		raise ValueError('options list cannot be empty! options='+str(options))
	print prompt
	try:
		choice = int(raw_input())
	except ValueError as e:
		print e.message
		choice = ''
	if choice in options:
		return options[choice]
	else:
		print str(choice) + '? I do not understand.'
		return getUserInput(options,prompt)

def startScript(path):
	"""
	starts script at given file loction (in form '/path/to/file.py') using import
	"""
	return imp.load_source('behaviorSimConfigScript', path)

def loadSample():
	"""
	Walks user through loading of a sample script.
	"""
	print 'choose from available sample scripts:'
	prompt,options = printFilesInDir(SAMPLES_PATH)
	choice = getUserInput(options,prompt)
	startScript(choice)

def loadScript():
	"""
	Walks user through loading of a script.
	"""
	print 'choose from your scripts:'
	prompt,options = printFilesInDir(SCRIPTS_PATH)
	if len(options) < 1:
		print 'ERR: you have no *.py scripts in ./scripts/'
		promptForScriptOrSample()
	else:
		choice = getUserInput(options,prompt)
		startScript(choice)

def startInteractive():
	"""load up a default environment and start python interactive mode"""
	from behaviorSim.simulation import simulation
	print 'loading simulation...'
	behaviorSim = simulation()
	print 'done.'
	
	print 'opening config util...'
	from behaviorSim.interface.CLI_config import CLI_config
	config = CLI_config()
	config.configure(behaviorSim)
	
	from behaviorSim.interface.CLI_run import CLI_run
	
	run = CLI_run()
	run.run(behaviorSim)
	
	print '\n\n starting interactive console with these values stored in object "behaviorSim". Have fun!\n\n'
	code.interact(local=locals())

def promptForScriptOrSample():
	"""
	Prompts the user to choose to load a sample or a personal script. Returns the value returned by chosen option function. 
	"""
	print	"""What would you like to do?:
	/t 1) load sample script (from '/example_scripts/')
	/t 2) load script (from '/scripts/')
	/t 3) load basic environment and start interactive mode
	"""
	options = {1 : loadSample,
	           2 : loadScript,
	           3 : startInteractive
	}
	try:
		choice = int(raw_input())
	except ValueError as e:
		print e.message
		choice = ''
	if choice in options:
		return options[choice]()
	else:
		print str(choice) + '? I do not understand.'
		return promptForScriptOrSample()

