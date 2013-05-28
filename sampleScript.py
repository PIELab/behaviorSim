# to load the 'standard' input and agent:
import inputs.inputs as inputs
import agents.agents as agents
sampleInput = inputs.inputs()
sampleAgent = agents.agents()

PAmodeli = model(runParams,inputs(),agent())	#???


# these agents can be modified/added to following editing instructions in ./inputs/inputs.py and ./agents/agents.py. 

print sampleInput.xi(5)		# print exogeneous flow vars @ t=5


# alternatively, specific instances of input/agents can be loaded directly like:
import inputs.PECS.example

print inputs.PECS.Example.belief(5)	# print belief @ t=5
