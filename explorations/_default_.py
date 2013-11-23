# -*- coding: utf-8 -*-
"""
Creates default display of simulation results.

Created on Sat Nov 23 12:11:45 2013

@author: tylar
"""

def explore(sim):
	if len(sim.environment.agents)<1:
		print 'Cannot create plots or infoFlow; no agents found in your simulation.'
		return
	else:
		print 'plotAll? (y/n)'
		choice = raw_input()
		while choice != 'n' and choice != 'y':
			print choice + '? please enter y or n.'
			choice = raw_input()
		if choice == 'y':
			print 'plottings all attributes for time 0 to 100'
			from behaviorSim.PECSplotter.plot import plotAll
			plotAll(sim.environment.agents[0],0,100)
			import pylab
			pylab.show()	
		
		print 'show infoFlow? (y/n)'
		choice = raw_input()
		while choice != 'n' and choice != 'y':
			print choice + '? please enter y or n.'
			choice = raw_input()
		if choice == 'y':
			import behaviorSim.PECSplotter.infoFlow as infoFlow
			infoFlow.showInfoFlow(sim.environment.agents[0])
		return