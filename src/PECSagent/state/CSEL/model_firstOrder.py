# first order fluid-flow model based on the theory of planned behavior

from pylab import array, linspace
from scipy import integrate	#for integrate.odeint

#globals:
beta = array([[0.0]*5]*5)
gamma = array([[0.0]*3]*5)
def fakeFunc(A,t): return -1.0 #fake function for allocating space
xi = fakeFunc
theta = array([0.0]*8)
tau   = array([0.0]*5)
samp = 0
ETA0 = array([0.0]*5)
ETADOT0 = [0.0]*5
time = linspace(0,0,0)	#(start,end,nSamples)
ETA = [integrate.odeint(fakeFunc,[ETA0[0],ETADOT0[0]],time),\
       integrate.odeint(fakeFunc,[ETA0[1],ETADOT0[1]],time),\
       integrate.odeint(fakeFunc,[ETA0[2],ETADOT0[2]],time),\
       integrate.odeint(fakeFunc,[ETA0[3],ETADOT0[3]],time),\
       integrate.odeint(fakeFunc,[ETA0[4],ETADOT0[4]],time)]

# method metadata:
	# time-invariant? = TRUE
	# (sim)time-dependent? = FALSE
# requirements for this method to be valid:
	# requiredTimeScale = days
	# requiredTimeStep  = 1
def model(data,t,BETA,GAMMA,XI,THETA,TAU):
	global beta, gamma, xi, theta, tau, samp, ETA, ETA0, ETADOT0
	beta = BETA
	gamma = GAMMA
	xi = XI
	theta = THETA
	tau = TAU
	ETA0 = getInitialEta()
	# set constants for function refs
	if t < len(data):
		return data[t]
	else:	# fill in data up to t
		if len(data) == 0:
			data.append(ETA0)
		else :
			ETA0 = data[0]
		steps = t	# steps to compute
		samp = 1	#samples per time step (must be 1?)
		time = linspace(len(data),t+1,samp*(steps))

		ETA[0] = integrate.odeint(eta1Func,[ETA0[0],ETADOT0[0]],time)
		#print ETA[0]
		ETA[1] = integrate.odeint(eta2Func,[ETA0[1],ETADOT0[1]],time)
		ETA[2] = integrate.odeint(eta3Func,[ETA0[2],ETADOT0[2]],time)
		ETA[3] = integrate.odeint(eta4Func,[ETA0[3],ETADOT0[3]],time)
		ETA[4] = integrate.odeint(eta5Func,[ETA0[4],ETADOT0[4]],time)

		for i in range(steps):
			data.append([ETA[0][i*samp,0],\
		                     ETA[1][i*samp,0],\
		                     ETA[2][i*samp,0],\
		                     ETA[3][i*samp,0],\
		                     ETA[4][i*samp,0]])
	return data[t]

# === PRIVATE METHODS ===

def eta1Func(A,t): 
	#these come from calling function
	global gamma, xi, theta, tau
	#print A
	eta = A[0]
	etaDot=A[1]
	#print '(gamma*xi(t-theta)-eta)/tau'
	#print '('+str(gamma[0,0])+'*'+str(xi(t-theta[0])[0])+'-'+str(eta)+')/' + str(tau[0]) + '='
	etaDDot= (gamma[0,0]*xi(t-theta[0])[0] - eta)/tau[0]
	#print etaDDot
	return checkValue(etaDDot)

def eta2Func(A,t): 
	#these come from calling function
	global gamma, xi, theta, tau
	eta    = A[0]
	etaDot = A[1]
	etaDDot= (gamma[1,1]*xi(t-theta[1])[1] - eta)/tau[1]
	return checkValue(etaDDot)

def eta3Func(A,t): 
	#these come from calling function
	global gamma, xi, theta, tau
	eta    = A[0]
	etaDot = A[1]
	etaDDot= (gamma[2,2]*xi(t-theta[2])[2] - eta)/tau[2]
	return checkValue(etaDDot)

def eta4Func(A,t): 
	#these come from calling function
	global beta, theta, tau
	eta    = A[0]
	etaDot = A[1]
	etaDDot= (   beta[3,0]*pastEta(t-theta[3],0) \
		 + beta[3,1]*pastEta(t-theta[4],1) \
		 + beta[3,2]*pastEta(t-theta[5],2) \
	         - eta)/tau[3]
	return checkValue(etaDDot)

def eta5Func(A,t): 
	#these come from calling function
	global beta, theta, tau
	eta    = A[0]
	etaDot = A[1]
	etaDDot= (   beta[4,3]*pastEta(t-theta[6],3) \
		 + beta[4,2]*pastEta(t-theta[7],2) \
	         - eta)/tau[4]
	return checkValue(etaDDot)

# values cannot fall below 0! ... or can they?
def checkValue(v):
	if v < 0 :
		return 0
	else:
		return v

#function to lookup a past eta (for time delays)
def pastEta(T,etaIndex):
	global deltaT, ETA, ETA0
	indexOfTime = int(round(T/samp))
	#print T
	if(indexOfTime<=0):
		return ETA0[etaIndex];
	elif(indexOfTime>=len(ETA)):
		return ETA[etaIndex][len(ETA)-1,0]
	else:
		
		#print ' time:',T
		#print 'index:',indexOfTime
		#print ' size:',size(ETA[etaIndex][indexOfTime][0])
		#print 'value:',ETA[etaIndex][indexOfTime,0]	#[eta#][time , eta_or_dEta]
		return ETA[etaIndex][indexOfTime,0]

#finds initial eta values based on steady-state assumption
def getInitialEta():
	global beta, gamma, xi
	eta0 = gamma[0,0]*xi(0)[0]
	eta1 = gamma[1,1]*xi(0)[1]
	eta2 = gamma[2,2]*xi(0)[2]
	eta3 = beta[3,0]*eta0 + beta[3,1]*eta1 + beta[3,2]*eta2
	eta4 = beta[4,3]*eta3 + beta[4,2]*eta2
	return array([eta0,eta1,eta2,eta3,eta4])

