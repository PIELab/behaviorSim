t = 5 	# time of interest

# === INPUTS ===
# load and use the 'standard' input:
import inputs.inputs as inputs
sampleInput1 = inputs.inputs()
print sampleInput1.xi(t)	# print exogeneous flow vars @ t=5

# this input can be modified/added to by following editing instructions in ./inputs/inputs.py

# alternatively, specific instances of input/agents can be loaded directly like:
import inputs.CSEL.example
print inputs.CSEL.example.xi(t)	# print belief @ t=5



# === AGENTS ===
# load and use the default agent:
import agent.agent as agent
sampleAgent1 = agent.agent()
# this agent can be modified/added to by following editing instructions in ./agent/agent.py

print sampleAgent1.P.getState(t)

# alternatively, load a custom instance of an agent directly:
#init agent data structures
#import agent.P.CSEL.state.example as Zp
#import agent.E.CSEL.state.example as Ze
#import agent.C.CSEL.state.example as Zc
#import agent.S.CSEL.state.example as Zs
#import agent.desires.CSEL.example as W
#import agent.output.CSEL.example  as Y
#sampleAgent2 = agent.agent(Zp,Ze,Zc,Zs,W,Y)

# load functions
#import agent.P.CSEL.internalModel.example as Fp
#import agent.E.CSEL.internalModel.example as Fe
#import agent.C.CSEL.internalModel.example as Fc
#import agent.S.CSEL.internalModel.example as Fs
#import agent.desireModel.CSEL.example as H
#import agent.outputModel.CSEL.example as G

#Fp.run(sampleAgent2)	#run the physical internalModel
#print sampleAgent.Zp(0)	#print first state of physical vars
#H.run(sampleAgent2)	#run the desireModel
#print sampleAgent.W(0)	#print first desire vars
#G.run(sampleAgent2)	#run the outputModel
#print sampleAgent2.Y(0)	#print first output




