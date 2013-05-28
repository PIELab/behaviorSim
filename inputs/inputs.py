# the inputs class initializes all possible inputs for the model, but calls external methods for loading the inputs. 

# set input file locations here:
from .CSEL import example as CSEL
# add new ones like this:
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

