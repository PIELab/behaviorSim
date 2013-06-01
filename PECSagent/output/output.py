# this file contains all information pertaining to the 'behaviors' AKA 'outputs' described in the PECS reference model

# === additions you might make are described in headers ===
# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
	# and encapsulated in arrows
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# === 1 import desired classes to define parts of input here ===
# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv

# from CSEL model
from .CSEL.behaviorDescriptor import outputKeys   as behaviorKeyGetter
from .CSEL.behaviorDescriptor import outputValues as behaviorValueGetter


# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

class output:
	# constructor
	def __init__(self,theInputs,theState,theMotivations):
		self.inputs     = theInputs
		self.state      = theState
		self.motivation = theMotivations
		# === define ALL raw data structures ===
		# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
		self.__behaviorKey=list()
		self.__behaviorValue=list()
		
		# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

	# returns ALL data for given time t as a dict 
	def __call__(self,t):
		# === 3 return ALL info for that time as a dict ===
		# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
		return dict(behaviorKey=self.behaviorKey(t),\
		            behaviorValue=self.behaviorValue(t))
		# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

	# === 4 define ALL getters using external functions ===
	# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
	# note: 'getters' are not true getters here; they also set.

	# describes the agent's behavior as a keyword (or list of keywords)
	def behaviorKey(self,t):
		return behaviorKeyGetter(self.__behaviorKey,t)

	# describes intensity of the behavior with a numerical value which (or list of values)
	def behaviorValue(self,t):
		return behaviorValueGetter(self.__behaviorValue,t,self.state.eta)
	
	# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

