# the environment class describes the world which is shared by all agents in the simulation. Agent inputs/context may be derived from the values in this environment

from behaviorSim.__util.agentData import dataObject

### define default functions
from attitudeInfluences.testAttitudes import squareWaves as influence_PAGetter
from attitudeInfluences.testAttitudes import someSteps   as _DFLT_FUNC_influence_EB
#from attitudeInfluences.CSELsteps     import pa          as influence_PAGetter

class environment(object):
	"""
	Defines an environment with which agents can interact.
	
	Attributes:
		name  = short string descriptor of env
		agents = list of agents in the environment
		
		width = physical dimension of environment grid
		height = ""
		
		dynamical values
			influence_EB = influence on eating behavior attitude
			influence_PA = influence on physical activity attitude
		
		location-dependent constant attributes:
			temperature = array of values defining temperature at location

	"""
	def __init__(self):
		#TODO: search for environment file name in settings
		#TODO: load named environment from given file
		#TODO: like this self.load('givenFile')

		#set up default environment otherwise
		print 'WARN: no environment file specified; using default'
		self.agents = list()

		#environment constants:
		self.name = 'defaultEnvironment'
		self.width = self.height = 100 

		#TODO: change this to use dataObject
		#time-dependent functions:
		self.__influence_PA = list()

		self.influence_EB = dataObject('influence_EB',_DFLT_FUNC_influence_EB)

		#environment maps (location dependent functions):
		self.temperature = [[[20]*self.width]*self.height]	#array of temperatures in degrees Celcius

	def __call__(self,t):
		"""
		Returns all data as dict for given time t
		"""
		self.influence_PA(t)
		self.influence_EB(t)
		
		return self.__dict__

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
