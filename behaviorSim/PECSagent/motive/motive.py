# the motive class contains all information pertaining to the 'motivation variables' AKA 'hidden variables' described in the PECS reference model

from ...__util.agentData import dataObject

### import default functions ###
from .baseInfo.death         import oldAger as _DFLT_FUNC_mortality
from .CSEL.behaviorTankValue import etaFive as _DFLT_FUNC_will_PA
from .CSEL.behaviorTankValue import etaFive as _DFLT_FUNC_will_EB



class motive:
	# constructor
	def __init__(self,state):

		### dataObjects ###

		# the agent's physiological succeptibility to death. 
		self.mortality=dataObject('mortality',_DFLT_FUNC_mortality, state.age)

		# the will of the agent to be physically active
		self.will_PA=dataObject('will_PA',_DFLT_FUNC_will_PA, state.eta_PA)
		
		# the will of the agent to be eat healthily
		self.will_EB=dataObject('will_EB',_DFLT_FUNC_will_EB, state.eta_EB)

	# returns ALL data for given time t as a dict 
	def __call__(self,t):
		### return ALL info for that time as a dict ###
		return self.__dict__
		#return dict(mortality=self.mortality(t),\
		#            will_PA=self.will_PA(t),\
		#            will_EB=self.will_EB(t))

