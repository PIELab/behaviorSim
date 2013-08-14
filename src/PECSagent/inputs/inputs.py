# the inputs class describes the context of the agent
#	dependencies:
#		environment = the environment which the agent is in

from ..settings import settings
from ...__util.agentData import dataObject

### import default functions ###
from .baseInfo.debugInfo  import currentTime as _DFLT_FUNC_initTime
from .baseInfo.timePassed import timePassed  as _DFLT_FUNC_time

from .CSEL.fromEnvironment import pa         as _DFLT_FUNC_attitudeChange_PA
from .CSEL.fromEnvironment import eb         as _DFLT_FUNC_attitudeChange_EB
from .CSEL.xi              import xi         as _DFLT_FUNC_xi

#TODO: xi not needed, since it is determined from attitudeChange values?


class inputs:	#can't use 'input' as the name b/c of built-in 'input()'
	# constructor
	def __init__(self,envir):
		self.environment = envir

		### create dataObjects ###

		# real-world time of calculation for each sim-world calculation of inputs
		self.initTime = dataObject('initTime',_DFLT_FUNC_initTime)

		# sim-world time of calculation
		self.time = dataObject('time',_DFLT_FUNC_time,settings.simStartTime,settings.deltaTime)

		## for Physical Activity (PA)
		#inflow to attitude about physical activity from theory of planned behavior
		self.attitudeChange_PA = dataObject('attitudeChange_PA',_DFLT_FUNC_attitudeChange_PA,self.environment)
		#exogenous flow variables from package CSEL
		self.xi_PA = dataObject('xi_PA',_DFLT_FUNC_xi,self.attitudeChange_PA)

		## for Eating Behavior (EB) ##
		#inflow to attitude about eating behaviors from theory of planned behavior
		self.attitudeChange_EB = dataObject('attitudeChange_EB',_DFLT_FUNC_attitudeChange_EB,self.environment)
		#exogenous flow variables from package CSEL
		self.xi_EB = dataObject('xi_EB',_DFLT_FUNC_xi,self.attitudeChange_EB)

		

	# returns ALL data for given time t as a dict 
	def __call__(self,t):
		### return ALL input info for that time as a dict ###
		return dict(initTime=self.initTime(t), \
		            time    =self.time(t),\
		            attitudeChange_PA=[self.attitudeChange_PA(t).behavioralBelief,\
		            self.attitudeChange_PA(t).behaviorAttitude,\
		            self.attitudeChange_PA(t).normativeBelief,\
		            self.attitudeChange_PA(t).subjectiveNorm,\
		            self.attitudeChange_PA(t).PBC,\
		            self.attitudeChange_PA(t).controlBelief],\
		            xi_PA           =str(self.xi_PA(t)),\
						attitudeChange_EB=[self.attitudeChange_EB(t).behavioralBelief,\
		            self.attitudeChange_EB(t).behaviorAttitude,\
		            self.attitudeChange_EB(t).normativeBelief,\
		            self.attitudeChange_EB(t).subjectiveNorm,\
		            self.attitudeChange_EB(t).PBC,\
		            self.attitudeChange_EB(t).controlBelief],\
		            xi_EB           =str(self.xi_EB(t)))

