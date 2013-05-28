from scipy import integrate	#for integrate.odeint
from pylab import array, linspace

import agent_default, inputs_constant 	#defaults (will be overwritten by values passed to class)

class model:
	# === RUN PARAMETERS:
#	#time window:
	START_TIME = 0.0
	END_TIME   = 0.0
	N_SAMPLES  = 0
	deltaT = 0;	#time step

	# === INITIAL CONDITIONS:	eta0 and etadot0
	ETA0    = [0.0,0.0,0.0,0.0,0.0]
	ETADOT0 = [0.0,0.0,0.0,0.0,0.0]

	# === MODEL OBJECTS:
	time = linspace(0,0,0)	
	theAgent = agent_default.agent()	#default agent
	theInput = inputs_constant.inputs()	#default agent

	# === OUTPUT:
	def fakeFunc(A,t): return 0 #fake function for allocating space
	ETA = [integrate.odeint(fakeFunc,[ETA0[0],ETADOT0[0]],time),\
	       integrate.odeint(fakeFunc,[ETA0[1],ETADOT0[1]],time),\
	       integrate.odeint(fakeFunc,[ETA0[2],ETADOT0[2]],time),\
	       integrate.odeint(fakeFunc,[ETA0[3],ETADOT0[3]],time),\
	       integrate.odeint(fakeFunc,[ETA0[4],ETADOT0[4]],time)]

	def __init__(self,params,daInput,daAgent):
		#time window:
		self.START_TIME = params.START_TIME
		self.END_TIME   = params.END_TIME
		self.N_SAMPLES  = params.N_SAMPLES
		self.deltaT     = abs(self.END_TIME-self.START_TIME)/self.N_SAMPLES;	#time step	

		self.time     = linspace(self.START_TIME,self.END_TIME,self.N_SAMPLES)	
		
		self.theAgent = daAgent
		self.theInput = daInput

		self.ETA0     = self.getInitialEta()
		self.ETADOT0  = [0.0,0.0,0.0,0.0,0.0]

		#solve the model
		self.ETA[0] = integrate.odeint(self.eta1Func,[self.ETA0[0],self.ETADOT0[0]],self.time)
		self.ETA[1] = integrate.odeint(self.eta2Func,[self.ETA0[1],self.ETADOT0[1]],self.time)
		self.ETA[2] = integrate.odeint(self.eta3Func,[self.ETA0[2],self.ETADOT0[2]],self.time)
		self.ETA[3] = integrate.odeint(self.eta4Func,[self.ETA0[3],self.ETADOT0[3]],self.time)
		self.ETA[4] = integrate.odeint(self.eta5Func,[self.ETA0[4],self.ETADOT0[4]],self.time)

	# values cannot fall below 0!
	def checkValue(self,v):
		return v

	def eta1Func(self,A,t): 
		eta    = A[0]
		etaDot = A[1]
		etaDDot= (self.theAgent.gamma[0,0]*self.theInput.xi(t-self.theAgent.theta[0])[0] - eta + self.theAgent.zeta(t,eta,0))/self.theAgent.tau[0]
		#print etaDDot
		return self.checkValue(etaDDot)

	def eta2Func(self,A,t): 
		eta    = A[0]
		etaDot = A[1]
		etaDDot= (self.theAgent.gamma[1,1]*self.theInput.xi(t-self.theAgent.theta[1])[1] - eta + self.theAgent.zeta(t,eta,1))/self.theAgent.tau[1]
		return self.checkValue(etaDDot)

	def eta3Func(self,A,t): 
		eta    = A[0]
		etaDot = A[1]
		etaDDot= (self.theAgent.gamma[2,2]*self.theInput.xi(t-self.theAgent.theta[2])[2] - eta + self.theAgent.zeta(t,eta,2))/self.theAgent.tau[2]
		return self.checkValue(etaDDot)

	def eta4Func(self,A,t): 
		eta    = A[0]
		etaDot = A[1]
		etaDDot= (   self.theAgent.beta[3,0]*self.pastEta(t-self.theAgent.theta[3],0) \
			 + self.theAgent.beta[3,1]*self.pastEta(t-self.theAgent.theta[4],1) \
			 + self.theAgent.beta[3,2]*self.pastEta(t-self.theAgent.theta[5],2) \
		         - eta + self.theAgent.zeta(t,eta,3) )/self.theAgent.tau[3]
		return self.checkValue(etaDDot)

	def eta5Func(self,A,t): 
		eta    = A[0]
		etaDot = A[1]
		etaDDot= (   self.theAgent.beta[4,3]*self.pastEta(t-self.theAgent.theta[6],3) \
			 + self.theAgent.beta[4,2]*self.pastEta(t-self.theAgent.theta[7],2) \
		         - eta + self.theAgent.zeta(t,eta,4))/self.theAgent.tau[4]
		return self.checkValue(etaDDot)

	#finds initial eta values based on steady-state assumption
	def getInitialEta(self):
		eta0 = self.theAgent.gamma[0,0]*self.theInput.xi(self.START_TIME)[0]
		eta1 = self.theAgent.gamma[1,1]*self.theInput.xi(self.START_TIME)[1]
		eta2 = self.theAgent.gamma[2,2]*self.theInput.xi(self.START_TIME)[2]
		eta3 = self.theAgent.beta[3,0]*eta0 + self.theAgent.beta[3,1]*eta1 + self.theAgent.beta[3,2]*eta2
		eta4 = self.theAgent.beta[4,3]*eta3 + self.theAgent.beta[4,2]*eta2
		return array([eta0,eta1,eta2,eta3,eta4])

	#function to lookup a past eta (for time delays)
	def pastEta(self,T,etaIndex):
		indexOfTime = int(round(T/self.deltaT))
		#print T
		if(indexOfTime<=0):
			return self.ETA0[etaIndex];
		elif(indexOfTime>=self.N_SAMPLES):
			return self.ETA[etaIndex][self.N_SAMPLES-1,0]
		else:
			
			#print ' time:',T
			#print 'index:',indexOfTime
			#print ' size:',size(ETA[etaIndex][indexOfTime][0])
			#print 'value:',ETA[etaIndex][indexOfTime,0]	#[eta#][time , eta_or_dEta]
			return self.ETA[etaIndex][indexOfTime,0]

