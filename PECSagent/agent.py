
from inputs.inputs         import inputs
from state.state           import state
from motivation.motivation import motivation
from output.output         import output

class agent:
	def __init__(self):
		self.inputs     = inputs()
		self.state      = state(self.inputs)
		self.motivation = motivation(self.state)
		self.output     = output(self.inputs,self.state,self.motivation)
