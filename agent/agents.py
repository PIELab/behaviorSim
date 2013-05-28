# the agents class defines the agent's behavior in terms of a behavioral model and calls external methods for loading the models based on the agentType (to match the model) and the specific agent being used (an instance of the agentType). Variations between instances of the same agentType are typically small such as differing coefficients.
# to organize this structure, agentTypes (or models) are subpackages of the agents package, and instances of the model are modules of the agentType package. Thus, the general structure is something like agents.model.instance to reference the desired module. When using different agents in a single simulation this can get very confusing. Thus, all agents are referenced through this agents class directly. That way this is the only file which needs to be changed when switching agents.

# set input file locations here:
#from .P.randomWalk import exmpl as P
#from .E.emotGuesser import xmpl as E
from .C.CSEL import example as C
#from .S.CSEL import example as S

# add new models like this:
# from .InputType import typeInstance as InputType

class agents:
	def __init__(self):
		# TODO: check input and print error if model/input mismatch?	

	# desired initialization must go here:
		# === CSEL ===
		
		# === yourNewInputType ===
		# add new ones here...

