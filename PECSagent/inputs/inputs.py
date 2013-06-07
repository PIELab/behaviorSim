# this 

# === additions you might make are described in headers ===
# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
	# and encapsulated in arrows
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

from ..settings import settings

# === 1 import desired classes to define parts of input here ===
# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
from .baseInfo.debugInfo  import currentTime  as initTimeGetter
from .baseInfo.timePassed import timePassed   as timeGetter
# from CSEL model
from .CSEL.attitudes import constAttitude as attitudeChange_PAGetter
from .CSEL.xi        import xi            as xiGetter

#TODO: xi not needed, since it is determined from attitude values?
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

class inputs:	#can't use 'input' as the name b/c of built-in 'input()'
	# constructor
	def __init__(self):
		# === define ALL raw data structures ===
		# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
		# from package debugInfo:
		self.__initTime=list()
		self.__time    =list()	# sim-world time of calculation
		# from package CSEL:
		self.__attitudeChange_PA=list()

		# TODO: add the other inputs which determine xi here OR remove all of them or xi (since they are a bit redundant)
		self.__xi           =list()
		
		# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

	# returns ALL data for given time t as a dict 
	def __call__(self,t):
		# === 3 return ALL info for that time as a dict ===
		# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
		return dict(initTime=self.initTime(t), \
		            time    =str(self.time(t)),\
		            attitudeChange_PA_behavioralBelief=str(self.attitudeChange_PA(t).behavioralBelief),\
		            attitudeChange_PA_behaviorAttitude=str(self.attitudeChange_PA(t).behaviorAttitude),\
		            attitudeChange_PA_normativeBelief=str(self.attitudeChange_PA(t).normativeBelief),\
		            attitudeChange_PA_subjectiveNorm=str(self.attitudeChange_PA(t).subjectiveNorm),\
		            attitudeChange_PA_PBC=str(self.attitudeChange_PA(t).PBC),\
		            attitudeChange_PA_controlBelief=str(self.attitudeChange_PA(t).controlBelief),\
		            xi           =str(self.xi(t)))
		# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

	# === 4 define ALL getters using external functions ===
	# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
	# note: 'getters' are not true getters here; they also set.

	# real-world time of calculation
	# from package debugInfo
	def initTime(self,t):
		return initTimeGetter(self.__initTime,t)

	# sim-world time of calculation
	# from package debugInfo
	def time(self,t):
		return timeGetter(self.__time,t,settings.simStartTime,settings.deltaTime)

	#attitude about physical activity
	# from package CSEL
	def attitudeChange_PA(self,t):
		return attitudeChange_PAGetter(self.__attitudeChange_PA,t)

	#exogenous flow variables
	# from package CSEL
	def xi(self,t):
		return xiGetter(self.__xi,t,self.attitudeChange_PA)
	
	# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

