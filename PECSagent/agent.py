
from inputs.inputs     import inputs
from state.state       import state
from motive.motive     import motive
from behavior.behavior import behavior

class agent:
	def __init__(self):
		self.inputs   = inputs()
		self.state    = state(self.inputs)
		self.motive   = motive(self.state)
		self.behavior = behavior(self.inputs,self.state,self.motive)
