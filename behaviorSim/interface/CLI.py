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

def startInteractive(sim):
	"""starts the python interactive console with simulation stored in memory"""
	behaviorSim = sim
	print '\n\n starting interactive console with simulation stored in object "behaviorSim". Have fun!\n\n'
	code.interact(local=locals())

def newExperiment():
	"""load up a default environment and start python interactive mode"""
	from behaviorSim.simulation import simulation
	print 'loading simulation...'
	behaviorSim = simulation()
	print 'done.'
	
	print 'opening config util...'
	from behaviorSim.interface.CLI_config import CLI_config
	CLI_config().configure(behaviorSim)
	
	from behaviorSim.interface.CLI_run import CLI_run
	CLI_run().run(behaviorSim)
	
	from behaviorSim.interface.CLI_explore import CLI_explore
	def runExploration():
		CLI_explore().explore(behaviorSim)
	runExploration()
	
	print 'simulation complete.'
	
	while(True):
		prompt = """What would you like to do now?
		 1) run another exploration script
		 2) open the python interactive console to explore manually
		 3) start over
		 4) exit"""
		options = {1 : runExploration,
		           2 : startInteractive,
		           3 : promptForScriptOrSample,
				4 : exit}
		choice = getUserInput(options,prompt)
		try: choice()
		except TypeError: #try passing the function simulation arg
			try: choice(behaviorSim)
			except: raise

def promptForScriptOrSample():
	"""
	Prompts the user to choose to load a sample or a personal script. Returns the value returned by chosen option function. 
	"""
	print	"""What would you like to do?:
	/t 1) create new simulation experiment
	/t 2) load experiment script (from '/scripts/')
	/t 3) load sample experiment script (from '/example_scripts/')
	"""
	options = {1 : newExperiment,
	           2 : loadScript,
	           3 : loadSample
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

