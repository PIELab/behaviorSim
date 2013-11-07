# first order fluid-flow model based on the theory of planned behavior
# NOTE: to re-enable debug printouts ctrl+h '	pass #logging.debug' and replace with 'logging.debug'

from pylab import array, linspace

import logging
from behaviorSim.__util.ddeint import *	#delay ode solver

from ...settings import settings

# === MODEL ===
# setup model functions:
def eta1func(eta1,t,xi,agent): 
	pass #logging.debug( '(agent(t).gamma*XI(t-agent(t).theta)-eta)/agent(t).tau' )
	pass #logging.debug( '('+str(agent(t).gamma[0,0])+'*'+str(xi(t-agent(t).theta[0])[0])+'-'+str(eta1(t))+')/' + str(agent(t).tau[0]) + '=' )
	etaDDot= (agent(t).gamma[0,0]*xi(t-agent(t).theta[0])[0] - eta1(t))/agent(t).tau[0]
	pass #logging.debug( 'eta1etaDDot='+str(etaDDot) )
	return etaDDot

def eta2func(eta2,t,xi,agent): 
	etaDDot= (agent(t).gamma[1,1]*xi(t-agent(t).theta[1])[1] - eta2(t))/agent(t).tau[1]
	return etaDDot

def eta3func(eta3,t,xi,agent): 
	etaDDot= (agent(t).gamma[2,2]*xi(t-agent(t).theta[2])[2] - eta3(t))/agent(t).tau[2]
	return etaDDot

def eta4func(eta4,t,agent,eta1,eta2,eta3): 
	etaDDot= (   agent(t).beta[3,0]*eta1(t-agent(t).theta[3]) \
		 + agent(t).beta[3,1]*eta2(t-agent(t).theta[4]) \
		 + agent(t).beta[3,2]*eta3(t-agent(t).theta[5]) \
	         - eta4(t))/agent(t).tau[3]
	return etaDDot

def eta5func(eta5,t,agent,eta3,eta4): 
	etaDDot= (   agent(t).beta[4,3]*eta4(t-agent(t).theta[6]) \
		 + agent(t).beta[4,2]*eta3(t-agent(t).theta[7]) \
	         - eta5(t))/agent(t).tau[4]
	return etaDDot

#finds initial eta values based on steady-state assumption
def steadyState(beta,gamma,xi):
	eta0 = gamma[0,0]*xi(0)[0]
	eta1 = gamma[1,1]*xi(0)[1]
	eta2 = gamma[2,2]*xi(0)[2]
	eta3 = beta[3,0]*eta0 + beta[3,1]*eta1 + beta[3,2]*eta2
	eta4 = beta[4,3]*eta3 + beta[4,2]*eta2
	return array([eta0,eta1,eta2,eta3,eta4])

# === SOLVER ===
def getEta(data,t,xi,agent):
#	print 'data='+str(data)
#	print 't='+str(t)
#	print 'xi='+str(xi)
#	print 'agent='+str(agent)
	if t < len(data):
		pass
	else:
		# === HISTORY === 
		# uses given data list to get historical eta
		def etaFromData(t,etaIndex):
			pass #logging.debug('looking up past eta'+str(etaIndex)+' at t='+str(t))
			if t > 0 and int(round(t)) < len(data):
				#indexOfT = int(round(float(t)/float(settings.subSteps)))
				indexOfT = int(round(t))
				pass #logging.debug(str(data))
				pass #logging.debug(str(data[indexOfT]))
				pass #logging.debug(str(data[indexOfT][etaIndex]))
				if data[indexOfT][etaIndex] + 7.77 < .0001:
					logging.warn('eta'+str(etaIndex)+' future state MAYBE requested')
				pass #logging.debug('returning past eta'+str(etaIndex)+' for time='+str(t)+' at index='+str(indexOfT))
				return data[indexOfT][etaIndex]
			elif t <= 0: #steady-state assumption
				pass #logging.debug('steady state value returned for eta'+str(etaIndex))
				return steadyState(agent(t).beta,agent(t).gamma,xi)[etaIndex]
			else :
				logging.warn('eta'+str(etaIndex)+' future state requested')
				return 0

		def etahist1(t) : 
			return etaFromData(t,0)
		def etahist2(t) : 
			return etaFromData(t,1)
		def etahist3(t) : 
			return etaFromData(t,2)
		def etahist4(t) : 
			return etaFromData(t,3)
		def etahist5(t) : 
			return etaFromData(t,4)

		# === SOLUTION ===
		if len(data) == 0: # initial value
			data.append(steadyState(agent(t).beta,agent(t).gamma,xi))
		for T in range(len(data),t+1):
			tt = linspace(T-1,T,settings.subSteps)
			pass #logging.debug('calculating eta over range '+str(T-1)+','+str(T))
			# append eta1 and fake data for others as placeholder
			data.append(array([ddeint(eta1func,etahist1,tt,fargs=(xi,agent(t)))[-1],\
			             -7.77,-7.77,-7.77,-7.77]))
			# then fill in real data as we get it...

			data[-1][1] = ddeint(eta2func,etahist2,tt,fargs=(xi,agent(t)))[-1]
 			data[-1][2] = ddeint(eta3func,etahist3,tt,fargs=(xi,agent(t)))[-1]
			pass #logging.debug('f_eta4('+str(T)+')='+str(data[-1][3]))
			data[-1][3] = ddeint(eta4func,etahist4,tt,fargs=(agent(t),etahist1,etahist2,etahist3))[-1]
			pass #logging.debug('f_eta4('+str(T)+')='+str(data[-1][3]))
			data[-1][4] = ddeint(eta5func,etahist5,tt,fargs=(agent(t),etahist3,etahist4))[-1]
	return data[t]

