# this 

# === additions you might make are described in headers ===
# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
	# and encapsulated in arrows
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# === 1 import desired classes to define parts of input here ===
# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
from .baseInfo.debugInfo  import currentTime as initTimeGetter
from .baseInfo.debugInfo  import pointless   as indexGetter
from .baseInfo.timePassed import timePassed  as timeGetter
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

class inputs:	#can't use 'input' as the name b/c of built-in 'input()'
	def __init__(self):
		self.deltaTime = 1	# sim-world time between steps
		self.timeUnits = 'days'	# sim-world time units
		# === define ALL raw data structures ===
		# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
		# from package debugInfo:
		self.__initTime=list()
		self.__index=list()	# index of indexed item (silly)
		self.__time=list()	# sim-world time of calculation
		# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

	def __call__(self,t):
		# === 3 return ALL info for that time as a dict ===
		# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
		return dict(initTime=self.initTime(t), \
		            index   =self.index(t), \
		            time    =str(self.time(t))+self.timeUnits)
		# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

	# === 4 define ALL getters using external functions ===
	# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
	# note: 'getters' are not true getters here; they also set.

	# real-world time of calculation
	def initTime(self,t):
		return initTimeGetter(self.__initTime,t)

	# index of indexed item (silly example method)
	def index(self,t):
		return indexGetter(self.__index,t)
	
	# sim-world time of calculation
	def time(self,t):
		return timeGetter(self.__time,t,self.deltaTime)

	# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

