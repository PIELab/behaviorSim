# -*- coding: utf-8 -*-
"""
agent environment configuration to recreate 
	Navarro-Barrientos, J.-E., Rivera, D. E., and Collins, L. M. "A
	dynamical model for describing behavioural interventions for weight
	loss and body composition change". Mathematical and computer
	modelling of dynamical systems 17, 2 (2011), 183–203.
	
In this context, "environment" is used to define the intervention.
"""

from datetime import datetime, timedelta

from behaviorSim.PECSagent.agent import agent
from behaviorSim.PECSagent.state.CSEL import agent_i, agent_ii, agent_iii
from behaviorSim.PECSagent.state.CSEL.model_ddeint_firstOrder_withDisturbances import getEta
from behaviorSim.PECSagent.inputs.CSEL.attitudes import stepOne

def configure(sim):
	"""use this function to configure the given simulation"""
	# customize settings
	sim.settings.deltaTime    = timedelta(days=1)
	sim.settings.simStartTime = datetime(2011, 1, 1, 12, 0, 0, 0)
	sim.settings.t0 = 0   #startTime
	sim.settings.tf = 180 #endTime

	# load agents personalities for i, ii, and iii
	agent1 = agent(sim.environment)
	agent1.state.setPersonality(agent_i.personality())
	
	agent2 = agent(sim.environment)
	agent2.state.setPersonality(agent_ii.personality())
	
	agent3 = agent(sim.environment)
	agent3.state.setPersonality(agent_iii.personality())
	
	#add disturbances
	agent3.state.eta_PA.setFunction(getEta,agent3.inputs.xi_PA,agent3.state.personality,agent3.state.zeta_PA)
	agent3.state.eta_EB.setFunction(getEta,agent3.inputs.xi_EB,agent3.state.personality,agent3.state.zeta_EB)
	
	# customize the CSEL input functions (exogeneous flow vars)
	def eatingAttitude(t):
		beforeChange = 7
		afterChange = 10
		changeT     = 10
		allOthers   = 1
		return stepOne(t,allOthers,'behavioralBelief',changeT,beforeChange,afterChange)
	agent1.inputs.attitudeChange_EB.setFunction(eatingAttitude)	#overwrite the default function
	agent2.inputs.attitudeChange_EB.setFunction(eatingAttitude)	#overwrite the default function
	agent3.inputs.attitudeChange_EB.setFunction(eatingAttitude)	#overwrite the default function
	
	def exerciseAttitude(t):
	# stepOne(data,t,value,steppedName,stepTime,beforeStep,afterStep):
		beforeChange = 1
		afterChange = 3
		changeT     = 30
		allOthers   = 1
		return stepOne(t,allOthers,'behavioralBelief',changeT,beforeChange,afterChange)
	agent1.inputs.attitudeChange_PA.setFunction(exerciseAttitude)	#overwrite the default function
	agent2.inputs.attitudeChange_PA.setFunction(exerciseAttitude)	#overwrite the default function
	agent3.inputs.attitudeChange_PA.setFunction(exerciseAttitude)	#overwrite the default function
	
	#sim.environment.addAgent(agent1)	
	#sim.environment.addAgent(agent2)	
	#sim.environment.addAgent(agent3)
