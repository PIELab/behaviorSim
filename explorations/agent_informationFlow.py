# -*- coding: utf-8 -*-
"""
This agent exploration script shows an information flow diagram for the agent.
The produced path diagram represents the flow of information between constructs
(dataObjects) to give an overview of the model behind the agent.

Created on Mon Nov 25 09:55:52 2013

@author: tylar
"""

import behaviorSim.PECSplotter.infoFlow as infoFlow

def explore(sim):
	for agent in sim.environment.agents:	
		infoFlow.showInfoFlow(agent)