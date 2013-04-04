# -*- coding: utf-8 -*-
from scipy import integrate
from pylab import * # for plotting commands

#show & save all relevant plots for given model, input
def makePlots(ETA,xi):
	figure()
	subplots_adjust(wspace=0.6)
	subplots_adjust(hspace=0.6)

	#inputs on the left (odds)
	subplot(421)
	plot([ xi(t*deltaT)[0] for t in range (N_SAMPLES) ]);
	ylabel('attitude (input; xi1)')
	ylim(0,90)
	grid(True)

	subplot(423)
	plot(0);
	ylabel('subjective norms in (xi2)')
	grid(True)

	subplot(425)
	plot(0);
	ylabel('PBC in (xi3)')
	grid(True)

	subplot(427)
	plot(0);
	ylabel('empty graph')
	grid(True)

	#outputs on the right (evens)
	subplot(422)
	plot(ETA[0][:,0]);
	ylabel('attitude (eta1)')
	ylim(0,90)
	grid(True)

	subplot(424)
	plot(ETA[3][:,0]);
	ylabel('intention (eta4)')
	ylim(0,70)
	grid(True)

	subplot(426)
	plot(ETA[4][:,0]);
	ylabel('behavior (eta5)')
	ylim(0,50)
	grid(True)

	subplot(428)
	plot(ETA[2][:,0]);
	#xlim(0,runParameters.timeToRun)
	#xlabel('time')
	ylabel('PBC (eta3)')
	grid(True)

	#TODO: what about socialNorms?

def getInitialEta():
	getEtaConsts()
	eta0 = gamma[0,0]*xi(START_TIME)[0]
	eta1 = gamma[1,1]*xi(START_TIME)[1]
	eta2 = gamma[2,2]*xi(START_TIME)[2]
	eta3 = beta[3,0]*eta0 + beta[3,1]*eta1 + beta[3,2]*eta2
	eta4 = beta[4,3]*eta3 + beta[4,2]*eta2
	return array([eta0,eta1,eta2,eta3,eta4])

def getEtaConsts():
	global xi,theta,tau,gamma,beta,zeta,pastEta
# given belief step function
	def belief(t):
		stepTime = 3;
		beforeStep = 4;
		afterStep = 6;
		if t < stepTime:
			return beforeStep;
		else: # t > stepTime
			return afterStep;
	
	# given outcome evaluation step function
	def outcomeEval(t):
		stepTime = 3;
		beforeStep = 2;
		afterStep = 6;
		if t < stepTime:
			return beforeStep;
		else: # t > stepTime
			return afterStep;

	def newXi(t):
		return array([belief(t)*outcomeEval(t), 1, 1]);
#	xi = array([[b1[t]*e1[t] for t in range(timeToRun)],	
#		    [1           for t in range(timeToRun)],
#		    [1           for t in range(timeToRun)]]);

	xi = newXi

	theta = array([0,0,0, 2,2,2,2,2]);	#time delays
	tau   = array([1,1,1, 2, 4]);		#time constants

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
		if(T<=START_TIME):
			return ETA0[etaIndex];
		elif(T>=END_TIME):
			return ETA[etaIndex][N_SAMPLES-1,0]
		else:
			indexOfTime = int(round(T/deltaT))
			#print ' time:',T
			#print 'index:',indexOfTime
			#print ' size:',size(ETA[etaIndex][indexOfTime][0])
			#print 'value:',ETA[etaIndex][indexOfTime,0]	#[eta#][time , eta_or_dEta]
			return ETA[etaIndex][indexOfTime,0]

	pastEta = newPastEta

def eta1Func(A,t): 
	eta    = A[0]
	etaDot = A[1]

	#set up constants. actual values come from getEtaConsts()

	getEtaConsts();

	return (gamma[0,0]*xi(t-theta[0])[0] - eta + zeta[0])/tau[0]

def eta2Func(A,t): 
	eta    = A[0]
	etaDot = A[1]

	getEtaConsts();

	return (gamma[1,1]*xi(t-theta[1])[1] - eta + zeta[1])/tau[1]

def eta3Func(A,t): 
	eta    = A[0]
	etaDot = A[1]

	getEtaConsts();

	return (gamma[2,2]*xi(t-theta[2])[2] - eta + zeta[2])/tau[2]

def eta4Func(A,t): 
	eta    = A[0]
	etaDot = A[1]

	getEtaConsts();

	return (   beta[3,0]*pastEta(t-theta[3],0) \
		     + beta[3,1]*pastEta(t-theta[4],1) \
		     + beta[3,2]*pastEta(t-theta[5],2) - eta+ zeta[3])/tau[3]

def eta5Func(A,t): 
	eta    = A[0]
	etaDot = A[1]

	getEtaConsts();

	return (   beta[4,3]*pastEta(t-theta[6],3) \
	             + beta[4,2]*pastEta(t-theta[7],2) - eta + zeta[4])/tau[4]

#time window:
START_TIME = 0.0
END_TIME   = 35.0
N_SAMPLES  = 1001
deltaT = abs(END_TIME-START_TIME)/N_SAMPLES;	#time step
time = linspace(START_TIME,END_TIME,N_SAMPLES)	

#initial conditions:	eta0 and etadot0
ETA0    = getInitialEta()
ETADOT0 = [0.0,0.0,0.0,0.0,0.0]
initCond = ETA0 + ETADOT0;	#append (not add)
def fakeFunc(A,t): return 0 #fake function for allocating space
ETA = [integrate.odeint(fakeFunc,[ETA0[0],ETADOT0[0]],time),\
       integrate.odeint(fakeFunc,[ETA0[1],ETADOT0[1]],time),\
       integrate.odeint(fakeFunc,[ETA0[2],ETADOT0[2]],time),\
       integrate.odeint(fakeFunc,[ETA0[3],ETADOT0[3]],time),\
       integrate.odeint(fakeFunc,[ETA0[4],ETADOT0[4]],time)]
ETA[0] = integrate.odeint(eta1Func,[ETA0[0],ETADOT0[0]],time)
ETA[1] = integrate.odeint(eta2Func,[ETA0[1],ETADOT0[1]],time)
ETA[2] = integrate.odeint(eta3Func,[ETA0[2],ETADOT0[2]],time)
ETA[3] = integrate.odeint(eta4Func,[ETA0[3],ETADOT0[3]],time)
ETA[4] = integrate.odeint(eta5Func,[ETA0[4],ETADOT0[4]],time)
#ETA1= ETA[:,0]

#print 'SIZE'
#print size(ETA[0][:,0])
getEtaConsts()	#gets xi to this level for makePlots
makePlots(ETA,xi)
#savefig('figures/CSELmodels');

figure()
#ylim(0,90)
grid(True)
for i in range(5):
	plot(time,ETA[i][:,0])
xlabel('t')
ylabel('eta')
show()
