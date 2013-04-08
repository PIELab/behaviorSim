from scipy import integrate	#for integrate.odeint
from pylab import * # for plotting commands & array

class secondOrderModel:
#	#time window:
	START_TIME = 0.0
	END_TIME   = 0.0
	N_SAMPLES  = 0
	deltaT = 0;	#time step

	#initial conditions:	eta0 and etadot0
	ETA0    = [0.0,0.0,0.0,0.0,0.0]
	ETADOT0 = [0.0,0.0,0.0,0.0,0.0]

	time = linspace(0,0,0)	
	def xi(t): return [0,0,0]
	def xiDot(self,t): 
		#this should be a pretty good estimate:
		dt = 1e-10
		res = ( (self.xi(t)-self.xi(t-dt)) + (self.xi(t+dt)-self.xi(t-dt)) )/2
		return res

	def fakeFunc(A,t): return 0 #fake function for allocating space
	ETA = [integrate.odeint(fakeFunc,[ETA0[0],ETADOT0[0]],time),\
	       integrate.odeint(fakeFunc,[ETA0[1],ETADOT0[1]],time),\
	       integrate.odeint(fakeFunc,[ETA0[2],ETADOT0[2]],time),\
	       integrate.odeint(fakeFunc,[ETA0[3],ETADOT0[3]],time),\
	       integrate.odeint(fakeFunc,[ETA0[4],ETADOT0[4]],time)]

	def __init__(self,params):
		global START_TIME,END_TIME,N_SAMPLES,deltaT,time,ETA0,ETADOT0
		#time window:
		self.START_TIME = params.START_TIME
		self.END_TIME   = params.END_TIME
		self.N_SAMPLES  = params.N_SAMPLES
		self.deltaT = abs(self.END_TIME-self.START_TIME)/self.N_SAMPLES;	#time step	

		self.time = linspace(self.START_TIME,self.END_TIME,self.N_SAMPLES)	
		self.ETA0    = self.getInitialEta()
		self.ETADOT0 = [0.0,0.0,0.0,0.0,0.0]

		#solve the model
		self.ETA[0] = integrate.odeint(self.eta1Func,[self.ETA0[0],self.ETADOT0[0]],self.time)
		self.ETA[1] = integrate.odeint(self.eta2Func,[self.ETA0[1],self.ETADOT0[1]],self.time)
		self.ETA[2] = integrate.odeint(self.eta3Func,[self.ETA0[2],self.ETADOT0[2]],self.time)
		self.ETA[3] = integrate.odeint(self.eta4Func,[self.ETA0[3],self.ETADOT0[3]],self.time)
		self.ETA[4] = integrate.odeint(self.eta5Func,[self.ETA0[4],self.ETADOT0[4]],self.time)

	def checkValue(self,v):
		#TODO: check for NaN etc...
		return v

	def eta1Func(self,state,t): 
		# unpack the state vector
		eta    = state[0]
		etaDot = state[1]
		self.getEtaConsts();
		#print '  eta:',eta
		#print ' etad:',etaDot
		etaDDot = ( gamma[0,0]*(self.xi(t-theta[0])[0] + tauA[0]*self.xiDot(t-theta[0])[0]) \
		           - eta + zeta[0] - 2*sigma*tau[0]*etaDot )/tau[0]**2
		etaDDot= self.checkValue(etaDDot)
		res = [etaDot,etaDDot]
		#print '  res:',res
		return res

	def eta2Func(self,state,t): 
		# unpack the state vector
		eta    = state[0]
		etaDot = state[1]
		self.getEtaConsts();

		etaDDot= (gamma[1,1]*(self.xi(t-theta[1])[1] + tauA[1]*self.xiDot(t-theta[1])[1]) - eta + zeta[1] - 2*sigma*tau[1]*etaDot)/tau[1]**2
		etaDDot= self.checkValue(etaDDot)
		return [etaDot,etaDDot]

	def eta3Func(self,state,t): 
		# unpack the state vector
		eta    = state[0]
		etaDot = state[1]
		self.getEtaConsts();

		etaDDot= (gamma[2,2]*(self.xi(t-theta[2])[2] + tauA[2]*self.xiDot(t-theta[2])[2]) - eta + zeta[2] - 2*sigma*tau[2]*etaDot)/tau[2]**2
		etaDDot= self.checkValue(etaDDot)
		return [etaDot,etaDDot]

# 1ST ORDER:
#	def eta4Func(self,A,t): 
#		eta    = A[0]
#		etaDot = A[1]
#
#		self.getEtaConsts();
#
#		return (   beta[3,0]*pastEta(t-theta[3],0) \
#			     + beta[3,1]*pastEta(t-theta[4],1) \
#			     + beta[3,2]*pastEta(t-theta[5],2) - eta+ zeta[3])/tau[3]
#
#	def eta5Func(self,A,t): 
#		eta    = A[0]
#		etaDot = A[1]
#
#		self.getEtaConsts();
#
#		return (   beta[4,3]*pastEta(t-theta[6],3) \
#			     + beta[4,2]*pastEta(t-theta[7],2) - eta + zeta[4])/tau[4]

# FIRSTGUESS:
#	def eta4Func(self,state,t): 
#		# unpack the state vector
#		eta    = state[0]
#		etaDot = state[1]
#		self.getEtaConsts()
#		 
#		A = beta[3,0]*pastEta(t-theta[3],0) \
#			       + beta[3,1]*pastEta(t-theta[4],1) \
#			       + beta[3,2]*pastEta(t-theta[5],2) \
#		               - eta + zeta[3] - 2*sigma*tau[3]*etaDot
#		#print 'eta4ish:',A
#		etaDDot = A /tau[3]**2
#		etaDDot= self.checkValue(etaDDot)
#		return [etaDot,etaDDot]
#
#	def eta5Func(self,state,t): 
#		# unpack the state vector
#		eta    = state[0]
#		etaDot = state[1]
#		self.getEtaConsts()
#
#		A = beta[4,3]*pastEta(t-theta[6],3) \
#			       + beta[4,2]*pastEta(t-theta[7],2) - eta + zeta[4] - 2*sigma*tau[3]*etaDot
#		#print 'eta5ish:',A
#		etaDDot =  A /tau[4] **2
#		etaDDot= self.checkValue(etaDDot)
#		return [etaDot,etaDDot]

# 2ND GUESS:
	def eta4Func(self,state,t): 
		# unpack the state vector
		eta    = state[0]
		etaDot = state[1]
		self.getEtaConsts()
		 
		A = beta[3,0]*( pastEta(t-theta[3],0) + tauA[3]*pastEtaDot(t-theta[3],0) ) \
		  + beta[3,1]*( pastEta(t-theta[4],1) + tauA[4]*pastEtaDot(t-theta[4],1) ) \
		  + beta[3,2]*( pastEta(t-theta[5],2) + tauA[5]*pastEtaDot(t-theta[5],2) ) \
		  - eta + zeta[3] - 2*sigma*tau[3]*etaDot
		#print 'eta4ish:',A
		etaDDot = A / tau[3]**2
		etaDDot= self.checkValue(etaDDot)
		return [etaDot,etaDDot]

	def eta5Func(self,state,t): 
		# unpack the state vector
		eta    = state[0]
		etaDot = state[1]
		self.getEtaConsts()

		A = beta[4,2]*( pastEta(t-theta[6],2) + tauA[6]*pastEtaDot(t-theta[6],2) ) \
		  + beta[4,3]*( pastEta(t-theta[7],3) + tauA[6]*pastEtaDot(t-theta[7],3) ) \
		  - eta + zeta[4] - 2*sigma*tau[3]*etaDot
		#print 'eta5ish:',A
		etaDDot =  A / tau[4] **2
		etaDDot= self.checkValue(etaDDot)
		return [etaDot,etaDDot]

	def getInitialEta(self):
		self.getEtaConsts()
		eta0 = gamma[0,0]*self.xi(self.START_TIME)[0]
		eta1 = gamma[1,1]*self.xi(self.START_TIME)[1]	
		eta2 = gamma[2,2]*self.xi(self.START_TIME)[2]
		eta3 = beta[3,0]*eta0 + beta[3,1]*eta1 + beta[3,2]*eta2
		eta4 = beta[4,3]*eta3 + beta[4,2]*eta2
		return array([eta0,eta1,eta2,eta3,eta4])

	def getEtaConsts(self):
		global theta,tau,gamma,beta,zeta,pastEta,pastEtaDot,tauA, sigma
	# given belief step function
		def belief(t):
			stepTime = 3;
			beforeStep = 4;
			afterStep = 8;
			if t < stepTime:
				return beforeStep;
			else: # t > stepTime
				return afterStep;
	
		# given outcome evaluation step function
		def outcomeEval(t):
			stepTime = 3;
			beforeStep = 2;
			afterStep = 8;
			if t < stepTime:
				return beforeStep;
			else: # t > stepTime
				return afterStep;

		def newXi(t):
			return array([belief(t)*outcomeEval(t), 1, 1]);
	#	xi = array([[b1[t]*e1[t] for t in range(timeToRun)],	
	#		    [1           for t in range(timeToRun)],
	#		    [1           for t in range(timeToRun)]]);

		self.xi = newXi

		theta = array([0,0,0,2,2,2,2,2]);	#time delays
		tau   = array([1,1,1,2,4]);		#time constants

		tauA  = array([-3,0,0,0,0,0,0,0]);
		sigma = 0.3;

		#exogenous inflow resistances:
		gamma = array([[1,1,1],\
			       [1,1,1],\
			       [1,1,1],\
			       [1,1,1],\
			       [1,1,1]]);

		#outflow resistance
		beta  = array([[0.5,0.5,0.5,0.5,0.5],\
			       [0.5,0.5,0.5,0.5,0.5],\
			       [0.5,0.5,0.5,0.5,0.5],\
			       [0.5,0.5,0.5,0.5,0.5],\
			       [0.5,0.5,0.5,0.5,0.5]]);

		# disturbances
		zeta= array([0,\
		       0,\
		       0,\
		       0,\
		       0]);

		#function to lookup a past eta (for time delays)
		def newPastEta(T,etaIndex):
			#print T
			if(T<=self.START_TIME):
				return self.ETA0[etaIndex];
			elif(T>=self.END_TIME):
				return self.ETA[etaIndex][self.N_SAMPLES-1,0]
			else:
				indexOfTime = int(round(T/self.deltaT)) - 1 #-1 b/c of starting @ 0
				#print ' time:',T
				#print 'index:',indexOfTime
				#print ' size:',size(ETA[etaIndex][indexOfTime][0])
				#print 'value:',ETA[etaIndex][indexOfTime,0]	#[eta#][time , eta_or_dEta]
				return self.ETA[etaIndex][indexOfTime,0]
		pastEta = newPastEta

		def newPastEtaDot(T,etaIndex):
			dT = 1e-10
			return ( (pastEta(T,etaIndex)-pastEta(T-dT,etaIndex)) + (pastEta(T+dT,etaIndex)-pastEta(T,etaIndex)) )/2
		pastEtaDot = newPastEtaDot
