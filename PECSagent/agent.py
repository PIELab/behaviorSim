
from inputs.inputs         import inputs
from state.state           import state
from motivation.motivation import motivation

class agent:
	def __init__(self):
		self.inputs     = inputs()
		self.state      = state(self.inputs)
		self.motivation = motivation(self.state)
