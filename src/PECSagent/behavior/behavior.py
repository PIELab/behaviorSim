# the behavior class defines information pertaining to the 'behaviors' AKA 'outputs' described in the PECS reference model
#	dependencies:
#		agent.state
#		agent.inputs
#		agent.motives

from ...__util.agentData import dataObject

### define default functions ###
from .CSEL.behaviorDescriptor import outputKeys   as behaviorKeyGetter
from .CSEL.behaviorDescriptor import outputValues as behaviorValueGetter



class behavior:
	# constructor
	def __init__(self,theInputs,theState,themotives):
		### dependencies ###
		self.inputs     = theInputs
		self.state      = theState
		self.motive = themotives

		### define dataObjects ###
		self.__behaviorKey=list()
		self.__behaviorValue=list()

		# === Behavioral intention and behavior ===
		#self.__behavioralIntention=list() ???
		#Behavioral intention: an indication of an individual's readiness to perform a given behavior. It is assumed to be an immediate antecedent of behavior (Ajzen, 2002b). It is based on attitude toward the behavior, subjective norm, and perceived behavioral control, with each predictor weighted for its importance in relation to the behavior and population of interest.
		#Behavior: an individual's observable response in a given situation with respect to a given target. Ajzen said a behavior is a function of compatible intentions and perceptions of behavioral control in that perceived behavioral control is expected to moderate the effect of intention on behavior, such that a favorable intention produces the behavior only when perceived behavioral control is strong.
		

	# returns ALL data for given time t as a dict 
	def __call__(self,t):
		### return ALL info for that time as a dict ###
		return dict(behaviorKey=self.behaviorKey(t),\
		            behaviorValue=self.behaviorValue(t))

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

