# first order fluid-flow model based on the theory of planned behavior

from pylab import array, linspace
from scipy import integrate	#for integrate.odeint

# setup logging
import logging
logging.basicConfig(filename='src/__logs/firstOrderModel2.log',\
                    level=logging.DEBUG,\
                    format='%(asctime)s %(levelname)s:%(message)s')

from .agent_defaultPersonality import agent as agentConstructor

#GLOBAL VARS:
agent = agentConstructor()
samp = 1	#samples per time step 
def fakeFunc(A,t): return -1.0 #fake function for allocating space
ETA = [integrate.odeint(fakeFunc,[0,0],linspace(0,1,10)),\
       integrate.odeint(fakeFunc,[0,0],linspace(0,1,10)),\
       integrate.odeint(fakeFunc,[0,0],linspace(0,1,10)),\
       integrate.odeint(fakeFunc,[0,0],linspace(0,1,10)),\
       integrate.odeint(fakeFunc,[0,0],linspace(0,1,10))]
XI = fakeFunc

def getEta(data,t,xi):
	global samp, ETA, time, agent, XI
	if t < len(data):
		return data[t]
	else:
		XI   = xi # update input function from paramteter
		if len(data) == 0:
			ETA0 = getInitialEta(agent.beta,agent.gamma,XI)
			data.append(ETA0[:])

		for T in range(len(data),t+1):
			# TODO: should this be samp*t so that accuracy is not lost far from 0???
			logging.info('solving ode @ t='+str(T)+', using '+str(samp)+' sub-samples')
			time = linspace(0,T,samp) #(start,end,nSamples)
			etadot_0 = [0,0,0,0,0]	#assumption of 1st order model
			#get arrays of data len=samp*t
			ETA[0] = integrate.odeint(eta1Func,[data[0][0],etadot_0[0]],time)
			ETA[1] = integrate.odeint(eta2Func,[data[0][1],etadot_0[1]],time)
			ETA[2] = integrate.odeint(eta3Func,[data[0][2],etadot_0[2]],time)
			ETA[3] = integrate.odeint(eta4Func,[data[0][3],etadot_0[3]],time)
			ETA[4] = integrate.odeint(eta5Func,[data[0][4],etadot_0[4]],time)
			logging.debug('len(result)='+str(len(ETA[0][:,0])))
			# restructure ETA using [eta#][time , eta_or_dEta] )
			E = [ETA[0][-1,0],\
			     ETA[1][-1,0],\
			     ETA[2][-1,0],\
			     ETA[3][-1,0],\
			     ETA[4][-1,0]]
			data.append(E)
		return data[t]
	
# === PRIVATE METHODS ===

def eta1Func(A,t): 
	#these come from calling function
	global XI, agent
	logging.debug( 'A='+str(A) )
	eta = A[0]
	etaDot=A[1]
	logging.debug( '(agent.gamma*XI(t-agent.theta)-eta)/agent.tau' )
	logging.debug( '('+str(agent.gamma[0,0])+'*'+str(XI(t-agent.theta[0])[0])+'-'+str(eta)+')/' + str(agent.tau[0]) + '=' )
	etaDDot= (agent.gamma[0,0]*XI(t-agent.theta[0])[0] - eta)/agent.tau[0]
	logging.debug( 'etaDDot='+str(etaDDot) )
	return checkValue(etaDDot)

def eta2Func(A,t): 
	#these come from calling function
	global XI, agent
	eta    = A[0]
	etaDot = A[1]
	etaDDot= (agent.gamma[1,1]*XI(t-agent.theta[1])[1] - eta)/agent.tau[1]
	return checkValue(etaDDot)

def eta3Func(A,t): 
	#these come from calling function
	global XI, agent
	eta    = A[0]
	etaDot = A[1]
	etaDDot= (agent.gamma[2,2]*XI(t-agent.theta[2])[2] - eta)/agent.tau[2]
	return checkValue(etaDDot)

def eta4Func(A,t): 
	#these come from calling function
	global agent
	eta    = A[0]
	etaDot = A[1]
	etaDDot= (   agent.beta[3,0]*pastEta(t-agent.theta[3],0) \
		 + agent.beta[3,1]*pastEta(t-agent.theta[4],1) \
		 + agent.beta[3,2]*pastEta(t-agent.theta[5],2) \
	         - eta)/agent.tau[3]
	return checkValue(etaDDot)

def eta5Func(A,t): 
	#these come from calling function
	global agent
	eta    = A[0]
	etaDot = A[1]
	etaDDot= (   agent.beta[4,3]*pastEta(t-agent.theta[6],3) \
		 + agent.beta[4,2]*pastEta(t-agent.theta[7],2) \
	         - eta)/agent.tau[4]
	return checkValue(etaDDot)

# values cannot fall below 0! ... or can they?
def checkValue(v):
	#logging.debug( 'val='+str(v) )
	return v
	#if v < 0 :
	#	return 0
	#else:
	#	return v

#finds initial eta values based on steady-state assumption
def getInitialEta(beta,gamma,xi):
	eta0 = gamma[0,0]*xi(0)[0]
	eta1 = gamma[1,1]*xi(0)[1]
	eta2 = gamma[2,2]*xi(0)[2]
	eta3 = beta[3,0]*eta0 + beta[3,1]*eta1 + beta[3,2]*eta2
	eta4 = beta[4,3]*eta3 + beta[4,2]*eta2
	return array([eta0,eta1,eta2,eta3,eta4])

#function to lookup a past eta (for time delays)
def pastEta(T,etaIndex):
	global ETA, samp, agent, XI
	indexOfTime = int(round(T/samp))
	#logging.debug( T )
	if(indexOfTime<=0):
		return getInitialEta(agent.beta,agent.gamma,XI);
	elif indexOfTime>=len(ETA[etaIndex][:,0]):
		logging.error('attempted reference to future Eta')
		return ETA[etaIndex][len(ETA)-1,0]
	else:
		logging.debug( ' time:'+str(T) )
		logging.debug( 'index:'+str(indexOfTime) )
		logging.debug( '  len:'+str(len(ETA[etaIndex][:,0])) )
		logging.debug( 'value:'+str(ETA[etaIndex][indexOfTime,0]) )	#[eta#][time , eta_or_dEta] )
		return ETA[etaIndex][indexOfTime,0]
