# -*- coding: utf-8 -*-
"""
Console interface for running a given simulation.

Created on Sat Nov 23 09:25:03 2013

@author: tylar
"""

from behaviorSim.__util.progressbar2_2.progressbar import ProgressBar

class CLI_run(object):
	def run(self,sim):
		print 'running simulation...'
		pbar = ProgressBar(maxval=sim.settings.tf).start()
		for i in range(sim.settings.t0,sim.settings.tf):
			pbar.update(i)
			for a in sim.environment.agents:
				a(i)
		pbar.finish()
		print 'done.'
