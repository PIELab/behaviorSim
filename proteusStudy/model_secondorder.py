from scipy import integrate	#for integrate.odeint
from pylab import array, linspace, size

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

	def xiDot(self,t): 
		#this should be a pretty good estimate:
		dt = 1e-10
		res = ( (self.theInput.xi(t)-self.theInput.xi(t-dt)) + (self.theInput.xi(t+dt)-self.theInput.xi(t-dt)) )/2
		return res

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

		self.ETA0     = self.getInitialEta()
		self.ETADOT0  = [0.0,0.0,0.0,0.0,0.0]
		
		self.theAgent = daAgent
		self.theInput = daInput

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

		etaDDot = ( self.theAgent.gamma[0,0]*(  self.theInput.xi(t-self.theAgent.theta[0])[0] \
		                                      + self.theAgent.tauA[0]*self.xiDot(t-self.theAgent.theta[0])[0]) \
		           - eta + self.theAgent.zeta(t,eta,0) - 2*self.theAgent.sigma*self.theAgent.tau[0]*etaDot )/self.theAgent.tau[0]**2
		res = [etaDot,etaDDot]
		return self.checkValue(res)

	def eta2Func(self,A,t): 
		eta    = A[0]
		etaDot = A[1]
		etaDDot= (self.theAgent.gamma[1,1]*(  self.theInput.xi(t-self.theAgent.theta[1])[1] \
		                                    + self.theAgent.tauA[1]*self.xiDot(t-self.theAgent.theta[1])[1]) \
		          - eta + self.theAgent.zeta(t,eta,1) - 2*self.theAgent.sigma*self.theAgent.tau[1]*etaDot)/self.theAgent.tau[1]**2
		res = [etaDot,etaDDot]
		return self.checkValue(res)


	def eta3Func(self,A,t): 
		eta    = A[0]
		etaDot = A[1]
		etaDDot= (self.theAgent.gamma[2,2]*(  self.theInput.xi(t-self.theAgent.theta[2])[2] \
		                                    + self.theAgent.tauA[2]*self.xiDot(t-self.theAgent.theta[2])[2]) \
		          - eta + self.theAgent.zeta(t,eta,2) - 2*self.theAgent.sigma*self.theAgent.tau[2]*etaDot)/self.theAgent.tau[2]**2
		res = [etaDot,etaDDot]
		return self.checkValue(res)

	def eta4Func(self,A,t): 
		eta    = A[0]
		etaDot = A[1]
		A = self.theAgent.beta[3,0]*( self.pastEta(t-self.theAgent.theta[3],0) \
		                            + self.theAgent.tauA[3]*self.pastEtaDot(t-self.theAgent.theta[3],0) ) \
		  + self.theAgent.beta[3,1]*( self.pastEta(t-self.theAgent.theta[4],1) \
		                            + self.theAgent.tauA[4]*self.pastEtaDot(t-self.theAgent.theta[4],1) ) \
		  + self.theAgent.beta[3,2]*( self.pastEta(t-self.theAgent.theta[5],2) \
		                            + self.theAgent.tauA[5]*self.pastEtaDot(t-self.theAgent.theta[5],2) ) \
		  - eta + self.theAgent.zeta(t,eta,3) - 2*self.theAgent.sigma*self.theAgent.tau[3]*etaDot
		etaDDot = A / self.theAgent.tau[3]**2
		res = [etaDot,etaDDot]
		return self.checkValue(res)

	def eta5Func(self,A,t): 
		eta    = A[0]
		etaDot = A[1]
		A = self.theAgent.beta[4,2]*( self.pastEta(t-self.theAgent.theta[6],2) \
		                            + self.theAgent.tauA[6]*self.pastEtaDot(t-self.theAgent.theta[6],2) ) \
		  + self.theAgent.beta[4,3]*( self.pastEta(t-self.theAgent.theta[7],3) \
		                            + self.theAgent.tauA[6]*self.pastEtaDot(t-self.theAgent.theta[7],3) ) \
		  - eta + self.theAgent.zeta(t,eta,4) - 2*self.theAgent.sigma*self.theAgent.tau[3]*etaDot
		etaDDot =  A / self.theAgent.tau[4] **2
		res = [etaDot,etaDDot]
		return self.checkValue(res)

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
		#print T
		if(T<=self.START_TIME):
			return self.ETA0[etaIndex];
		elif(T>=self.END_TIME):
			return self.ETA[etaIndex][self.N_SAMPLES-1,0]
		else:
			indexOfTime = int(round(T/self.deltaT))
			#print ' time:',T
			#print 'index:',indexOfTime
			#print ' size:',size(ETA[etaIndex][indexOfTime][0])
			#print 'value:',ETA[etaIndex][indexOfTime,0]	#[eta#][time , eta_or_dEta]
			return self.ETA[etaIndex][indexOfTime,0]

	def pastEtaDot(self,T,etaIndex):
		dT = 1e-10
		return ( (self.pastEta(T,etaIndex)-self.pastEta(T-dT,etaIndex)) + (self.pastEta(T+dT,etaIndex)-self.pastEta(T,etaIndex)) )/2
