# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 18:42:20 2013

@author: 7yl4r
"""

import unittest
import behaviorSim.API as API

from behaviorSim.__util.setupLog import setupLog
setupLog()

from behaviorSim.PECSagent.state.baseInfo.name import iterativeNamer as nameSetter
from random import randrange



class basicAPI_Test(unittest.TestCase):

	def setUp(self):
		self.defSim = API.getDefaultSimulation()

		self.defEnv = API.getDefaultEnvironment()

		self.defAgent = API.getDefaultAgent(self.defEnv)

	def test_basicLoadNoCrash(self):
		self.defSim = API.getDefaultSimulation()

		self.defEnv = API.getDefaultEnvironment()

		self.defAgent = API.getDefaultAgent(self.defEnv)

	#TODO: add testing of all configuration scripts in config script dir

	#TODO: add testing of all exploration scripts in exploration dir, suppress outputs

	def test_customizeAgent(self):
		API.removeConstruct(self.defAgent.state,'name')

		with self.assertRaises(AttributeError):
			self.defAgent.state.name

		newNameObj = API.getConstruct('name',nameSetter() )
		API.addConstruct(self.defAgent.state,newNameObj)

		t = randrange(10)
		self.assertTrue(newNameObj(t) == self.defAgent.state.name(t))