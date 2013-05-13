# this file is used to specify constants for CSEL model which effect the agent's (participant's) 'personality'

from pylab import array
from random import random

class agent:
	theta = array([0,0,0,2,2,2,15,2]);	#time delays
	tau   = array([20,1,1, 2, 4]);		#time constants

	# exogenous inflow resistances:
	gamma = array([[1,1,1],\
		       [1,1,1],\
		       [1,1,1],\
		       [1,1,1],\
		       [1,1,1]]);

	# outflow resistances (depletion constants)
	beta  = array([[0.5,0.5,0.5,0.5,0.5],\
		       [0.5,0.5,0.5,0.5,0.5],\
		       [0.5,0.5,0.5,0.5,0.5],\
		       [0.5,0.5,0.5,0.5,0.5],\
		       [0.5,0.5,0  ,0.5,0.5]]);

	# disturbances
	def zeta(self,t,currentValue,index):
		return 0	#real disturbances added after (since I can't get this to work)

	# === for 2nd order model only: === 
	tauA  = array([-3,0,0,0,0,0,0,0]);
	sigma = 0.3;	# there are actually several different sigma, but they are all the same in the paper TODO: change this. 
