#from ..PECSagent.agent import agent
from attitudeInfluences.PA import squareWaves as influence_PAGetter

class environment(object):
	def __init__(self):
		#TODO: search for environment file name in settings
		#TODO: load named environment from given file
		#TODO: like this self.load('givenFile')

		#set up default environment otherwise
		print 'WARN: no environment file specified; using default'
		self.agents = list()

		#environment constants:
		self.name = 'defaultEnvironment'
		self.width = self.height = 100 #physical dimensions of environment grid

		#time-dependent functions:
		self.__influence_PA = list()

		#environment maps (location dependent functions):
		self.temperature = [[[20]*self.width]*self.height]	#array of temperatures in degrees Celcius


	#TODO: implement the following function:
	#load environment from given file
	def load(self,fileName):
		self.agents = list()
		#import fileName
		#fileName.setupOrSomething(self)
		
	#influence on agent opinion of physical activity
	def influence_PA(self,t):
		return influence_PAGetter(self.__influence_PA,t)

	#add an agent to this environment
	def addAgent(self,agent):
		agent.environmentName = self.name
		self.agents.append(agent)

	def getName(self):
		return self.name
