# this 

# === additions you might make are described in headers ===
# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
	# and encapsulated in arrows
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

from ..settings import settings
from ...__util.agentData import dataObject

# === 1 import desired classes to define parts of input here ===
# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
from .baseInfo.debugInfo  import currentTime  as initTimeGetter
from .baseInfo.timePassed import timePassed   as timeGetter

from .CSEL.fromEnvironment import pa as attitudeChange_PAGetter
from .CSEL.xi        import xi            as xiGetter

#TODO: xi not needed, since it is determined from attitude values?
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

class inputs:	#can't use 'input' as the name b/c of built-in 'input()'
	# constructor
	def __init__(self,envir):
		self.environment = envir

		# real-world time of calculation for each sim-world calculation of inputs
		self.initTime = dataObject(initTimeGetter)

		# sim-world time of calculation
		self.time = dataObject(timeGetter,settings.simStartTime,settings.deltaTime)

		#attitude about physical activity from theory of planned behavior
		self.attitudeChange_PA = dataObject(attitudeChange_PAGetter,self.environment)

		#exogenous flow variables from package CSEL
		self.xi = dataObject(xiGetter,self.attitudeChange_PA)
		

	# returns ALL data for given time t as a dict 
	def __call__(self,t):
		# === 3 return ALL input info for that time as a dict ===
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

