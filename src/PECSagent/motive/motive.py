# the motive class contains all information pertaining to the 'motivation variables' AKA 'hidden variables' described in the PECS reference model

### import default functions ###
from .baseInfo.death  import oldAger  as mortalityGetter

# from CSEL model
from .CSEL.behaviorTankValue import etaFive as will_PAGetter



class motive:
	# constructor
	def __init__(self,theStates):
		self.state = theStates
		# === define ALL raw data structures ===

		# from package baseInfo:
		self.__mortality=list()
		# from package CSEL:
		self.__will_PA=list()
		

	# returns ALL data for given time t as a dict 
	def __call__(self,t):
		### return ALL info for that time as a dict ###
		return dict(mortality=self.mortality(t),\
		            will_PA=self.will_PA(t))

	# === 4 define ALL getters using external functions ===
	# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
	# note: 'getters' are not true getters here; they also set.

	# describes the agent's physiological succeptibility to death. 
	# from package baseInfo
	def mortality(self,t):
		return mortalityGetter(self.__mortality,t,self.state.age)

	# represents the will of the agent to be physically active
	# from package CSEL 
	def will_PA(self,t):
		return will_PAGetter(self.__will_PA,t,self.state.eta)
	
	# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

