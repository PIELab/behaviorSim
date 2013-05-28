# this file is used to specify constants for CSEL model which effect the agent's (participant's) 'personality'

from pylab import array
import random

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
	
	# disturbances TODO: this does not work (and I have no idea why)
	def zeta(self,t,currentValue,index):
		if index < 1:
			random.seed(t)
			r = random.random()
			print 'rand@seed',t,':',r
			return r
		else:
			return 0



#		if index > 0:
#			return 0
#		else:
#			maxV = 20	# maximum value
#			minV = 0	# minimum value
#			maxAmplitude = .009	# max of disturbance
#			dist = (0.5-random())*2.0 * maxAmplitude
			#print dist
			#make sure resulting eta will be within bounds
#			if currentValue + dist >= maxV:
#				return -1.0
#			elif currentValue + dist <= minV:
#				return 1.0
#			else:
#				return dist

	# === for 2nd order model only: === 
	tauA  = array([-3,0,0,0,0,0,0,0]);
	sigma = 0.3;	# there are actually several different sigma, but they are all the same in the paper TODO: change this. 
