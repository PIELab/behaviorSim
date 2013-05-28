# the inputs class initializes inputs for the model and calls external methods for loading the inputs based on the inputType (to match the model) and the specific input being used (an instance of the inputType). 
# to organize this structure, inputTypes (or models) are subpackages of the inputs package, and instances of the model are modules of the inputType package. Thus, the general structure is something like inputs.model.instance to reference the desired module. This is particularly troublesome when a specific input may be used by more than one model or when combining two models. To simplify references to input, all input is referenced through this inputs class directly. That way this is the only file which needs to be changed when switching inputs.

# set input file locations here:
from .CSEL import example as CSEL
#alternative model instance:
#from .CSEL import otherExample as CSEL

# add new models like this:
# from .InputType import typeInstance as InputType

class inputs:
	def __init__(self):

	# TODO: include a list of loaded input types for checking later?	

	# desired input initialization must go here:
		# === CSEL ===
		self.belief = CSEL.getBelief()
		self.outcomeEval = CSEL.getOutcomeEval()
		self.xi = CSEL.getXi()
		# === yourNewInputType ===
		# add new ones here...

