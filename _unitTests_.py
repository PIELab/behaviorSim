# this file is used to run unit tests on various code bits

import unittest
import random
from time import time

# setup logging
import logging
from behaviorSim.__util.setupLog import setupLog
setupLog()

class testAgentData(unittest.TestCase):

	def setUp(self):
		self.randCoeff = random.uniform(-1.0,1.0)

	def linearTestFunc(self,t):
		"""Simple linear time-dependent function."""
		return t

	def calcCheck(self, d, testF, t0, tf):
		"""checks that d(t) and testF(t) return the same for times from t0 to tf"""
		for t in range(t0,tf):
			self.assertTrue( d(t) == self.linearTestFunc(t) )

	def test_dataObjectInit(self):
		from behaviorSim.__util.agentData import dataObject

		D = dataObject('testObject',self.linearTestFunc)

		start_time = time()
		N = 100000
		# initial calculation
		self.calcCheck(D, self.linearTestFunc, 0, N)
		t1 = time()-start_time

		# 2nd time is just retrieval, should be faster (calculation is more complex than lookup)
		self.calcCheck(D, self.linearTestFunc, 0, N)
		t2 = time()-start_time-t1
		print 't/calc=', t1/N, ' t/lookup=', t2/N
		self.assertTrue( t1 >= t2 ) 
	
if __name__ == '__main__':
    unittest.main()

