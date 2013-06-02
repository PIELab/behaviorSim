
from inputs.inputs import inputs
from state.state   import state
from motive.motive import motive
from output.output import output

class agent:
	def __init__(self):
		self.inputs = inputs()
		self.state  = state(self.inputs)
		self.motive = motive(self.state)
		self.output = output(self.inputs,self.state,self.motivation)
