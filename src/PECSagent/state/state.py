# this file encapsulates all information pertaining to the state of the agent

# === additions you might make are described in headers ===
# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
	# and encapsulated in arrows
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

from ..settings import settings

# setup logging
import logging
logging.basicConfig(filename='src/__logs/state.log',\
                    level=logging.DEBUG,\
                    format='%(asctime)s %(levelname)s:%(message)s')

# === 1 import desired classes to define parts of input here ===
# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
from .baseInfo.age  import age            as ageGetter
from .baseInfo.age  import randomAger     as birthdaySetter
from .baseInfo.name import iterativeNamer as nameSetter
# from CSEL model:
from .CSEL.disturbances      import gaussZeta  as zetaGetter
from .CSEL.model_ddeint_firstOrder  import getEta     as etaGetter

from .CSEL.agent_defaultPersonality import agent as agentConstructor

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

class state:	#can't use 'input' as the name b/c of built-in 'input()'
	# constructor
	def __init__(self,theInputs):
		self.inputs   = theInputs
	# === define ALL raw data structures ===
	# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
		# constant attributes (personality):
		# from package baseInfo:
		self.name     = nameSetter()
		self.birthday = birthdaySetter(settings.simStartTime)
		self.agentPersonality = agentConstructor()

		# (potentially) time-variant attributes:
		# from package baseInfo:
		self.__age = list()
		# from package CSEL:
		self.__zeta = list()
		self.__eta  = list()

		
		
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
	
	# array of random distubances into the endogeneous flow vars, eta
	# from package CSEL
	def zeta(self,t):
		return zetaGetter(self.__zeta,t)

	# array of endogeneous flow variables
	# from package CSEL
	def eta(self,t):
		et = etaGetter(self.__eta,t,self.inputs.xi,self.agentPersonality)
		e = list()
		for etaIndex in range(len(et)):
			e.append(et[etaIndex] + self.zeta(t)[etaIndex])
		return e

	# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

