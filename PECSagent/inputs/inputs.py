# this 

# === additions you might make are described in headers ===
# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
	# and encapsulated in arrows
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

from ..settings import settings

# === 1 import desired classes to define parts of input here ===
# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
from .baseInfo.debugInfo  import currentTime  as initTimeGetter
from .baseInfo.debugInfo  import pointless    as indexGetter
from .baseInfo.timePassed import timePassed   as timeGetter
# from CSEL model
from .CSEL.inputs_constant import belief      as PAbeliefGetter
from .CSEL.inputs_constant import outcomeEval as PAoutcomeEvalGetter
#TODO: other metrics which determine exogenous flow vars here
from .CSEL.inputs_constant import xi          as xiGetter	#TODO: xi not needed, since it is determined from above values?
#TODO: xi should be split into PBC, attitude, etc...?
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

class inputs:	#can't use 'input' as the name b/c of built-in 'input()'
	# constructor
	def __init__(self):
		# === define ALL raw data structures ===
		# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
		# from package debugInfo:
		self.__initTime=list()
		self.__index   =list()	# index of indexed item (silly)
		self.__time    =list()	# sim-world time of calculation
		# from package CSEL:
		self.__PAbelief     =list()
		self.__PAoutcomeEval=list()
		self.__xi           =list()
		
		# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

	# returns ALL data for given time t as a dict 
	def __call__(self,t):
		# === 3 return ALL info for that time as a dict ===
		# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
		return dict(initTime=self.initTime(t), \
		            index   =self.index(t), \
		            time    =str(self.time(t))+settings.timeUnits,\
		            PAbelief=str(self.PAbelief(t)),\
		            PAoutcomeEval=str(self.PAoutcomeEval(t)),\
		            xi           =str(self.xi(t)))
		# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

	# === 4 define ALL getters using external functions ===
	# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
	# note: 'getters' are not true getters here; they also set.

	# real-world time of calculation
	# from package debugInfo
	def initTime(self,t):
		return initTimeGetter(self.__initTime,t)
	# index of indexed item (silly example method)
	# from package debugInfo
	def index(self,t):
		return indexGetter(self.__index,t)
	# sim-world time of calculation
	# from package debugInfo
	def time(self,t):
		return timeGetter(self.__time,t,settings.deltaTime)

	# belief about physical activity
	# from package CSEL
	def PAbelief(self,t):
		return PAbeliefGetter(self.__PAbelief,t)
	# evaluation of physical activity outcomes
	# from package CSEL
	def PAoutcomeEval(self,t):
		return PAoutcomeEvalGetter(self.__PAoutcomeEval,t)
	#exogenous flow variables
	# from package CSEL
	def xi(self,t):
		return xiGetter(self.__xi,t,self.PAbelief(t),self.PAoutcomeEval(t))
	
	# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

