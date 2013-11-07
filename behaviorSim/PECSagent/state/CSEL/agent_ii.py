# this file is used to specify constants for CSEL model which effect the agent's (participant's) 'personality'

from pylab import array

		# TODO: give these better names!
#		self.theta    = CSELagent.theta	#time delays
#		self.tau      = CSELagent.tau	#time constants
#		self.gamma    = CSELagent.gamma	#inflow resistances
#		self.beta     = CSELagent.beta	#outflow resists (depletion constants)
#		self.tauA     = CSELagent.tauA	
#		self.sigma    = CSELagent.sigma	

class personality:
	def __call__(self,t):
			return self

	disturbancesOn = False

	name  = 'agentII'
	theta = array([0,0,0, 2,2,2,0,15]);	#time delays
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
		       [0.5,0.5,  0,0.5,0.5]]);


	# === for 2nd order model only: === 
	tauA  = array([-3,0,0,0,0,0,0,0]); #2nd order time const
	sigma = 0.3; # deriv flow resists? # there are actually several different sigma, but they are all the same in the paper TODO: change this. 
