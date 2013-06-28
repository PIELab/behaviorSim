# based on:
#J.-Emeterio Navarro-Barrientos , Daniel E. Rivera & Linda M. Collins (2011):
#A dynamical model for describing behavioural interventions for weight loss and body composition
#change, Mathematical and Computer Modelling of Dynamical Systems: Methods, Tools and
#Applications in Engineering and Related Sciences, 17:2, 183-203

from pylab import array
from math import ceil
from src.__util.agentData import linearInterpolate

# xi = exogeneous inflow array = [ attitude, social norm, planned behavioral control ]
def xi(past,t,attitude):
	a = attitude(t)
	x1 = a.behavioralBelief*a.behaviorAttitude
	x2 = a.normativeBelief*a.subjectiveNorm
	x3 = a.PBC*a.controlBelief
	return array([x1,x2,x3])

