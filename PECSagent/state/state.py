# this file encapsulates all information pertaining to the state of the agent

# === additions you might make are described in headers ===
# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
	# and encapsulated in arrows
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

from ..settings import settings

# === 1 import desired classes to define parts of input here ===
# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
from .baseInfo.age  import age            as ageGetter
from .baseInfo.age  import randomAger     as birthdaySetter
from .baseInfo.name import iterativeNamer as nameSetter
# from CSEL model:
from .CSEL.agent_default import agent     as CSELagent
from .CSEL.disturbances  import gaussZeta as zetaGetter

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

class state:	#can't use 'input' as the name b/c of built-in 'input()'
	# constructor
	def __init__(self):
	# === define ALL raw data structures ===
	# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
		# constant attributes:
		# from package baseInfo:
		self.name     = nameSetter()
		self.birthday = birthdaySetter(settings.simStartTime)
		#from package CSEL:
		# TODO: give these better names!
		self.theta    = CSELagent.theta
		self.tau      = CSELagent.tau
		self.gamma    = CSELagent.gamma
		self.beta     = CSELagent.beta
		self.tauA     = CSELagent.tauA
		self.sigma    = CSELagent.sigma

		# (potentially) time-variant attributes:
		# from package baseInfo:
		self.__age=list()
		# from package CSEL:
		self.__zeta=list()

		
		
	# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

	# returns ALL data for given time t as a dict 
	def __call__(self,t):
		# === 3 return ALL info for that time as a dict ===
		# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
		return dict(agentName=self.name,\
		            birthday=self.birthday,\
		            age     =self.age(t))
		# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

	# === 4 define ALL getters using external functions ===
	# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
	# note: 'getters' are not true getters here; they also set.

	# sim-world age of agent
	# from package baseInfo
	def age(self,t):
		return ageGetter(self.__age,t,self.birthday,settings.deltaTime,settings.simStartTime)
	
	# array of random distubances on the flows between vars
	# from package CSEL
	def zeta(self,t):
		return zetaGetter(self.__zeta,t)	

	# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

