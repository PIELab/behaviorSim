# the motive class contains all information pertaining to the 'motivation variables' AKA 'hidden variables' described in the PECS reference model

from ...__util.agentData import dataObject

### import default functions ###
from .baseInfo.death         import oldAger as _DFLT_FUNC_mortality
from .CSEL.behaviorTankValue import etaFive as _DFLT_FUNC_will_PA



class motive:
	# constructor
	def __init__(self,state):

		### dataObjects ###

		# the agent's physiological succeptibility to death. 
		self.mortality=dataObject(_DFLT_FUNC_mortality, state.age)

		# the will of the agent to be physically active
		self.will_PA=dataObject(_DFLT_FUNC_will_PA, state.eta)
		

	# returns ALL data for given time t as a dict 
	def __call__(self,t):
		### return ALL info for that time as a dict ###
		return dict(mortality=self.mortality(t),\
		            will_PA=self.will_PA(t))

