# based on:
#J.-Emeterio Navarro-Barrientos , Daniel E. Rivera & Linda M. Collins (2011):
#A dynamical model for describing behavioural interventions for weight loss and body composition
#change, Mathematical and Computer Modelling of Dynamical Systems: Methods, Tools and
#Applications in Engineering and Related Sciences, 17:2, 183-203

from pylab import array
from math import ceil, floor

# xi = exogeneous inflow array = [ attitude, social norm, planned behavioral control ]
def xi(data,t,attitude):
	if t+1 < len(data):
		return linearInterpolate(data,t)
	else:
		for i in range(len(data),int(ceil(t+1))):
			a = attitude(i)
			x1 = a.behavioralBelief*a.behaviorAttitude
			x2 = a.normativeBelief*a.subjectiveNorm
			x3 = a.PBC*a.controlBelief
			data.append(array([x1,x2,x3]))	
		return linearInterpolate(data,t)


def linearInterpolate(data,t):
	if t%1 < .0001 or t%1 >.9999:	#if t is really close to int
		return data[int(t)]
	else:
		#linearly interpolate between data points
		m = data[int(ceil(t))]-data[int(floor(t))]	#slope
		x = t%1	#dist from known value
		b = floor(t)	#known value
		return m*x + b
