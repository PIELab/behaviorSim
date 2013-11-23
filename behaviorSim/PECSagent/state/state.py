# the state class encapsulates all information pertaining to the internal state variables of the agent

from ..settings import settings
from ...__util.agentData import dataObject

import logging

### import personality setters ###
from .baseInfo.age  import randomAger     as birthdaySetter
from .baseInfo.name import iterativeNamer as nameSetter

from .CSEL.agent_defaultPersonality import personality      as agentConstructor

### import default functions for data ###
from .baseInfo.age                  import age        as _DFLT_FUNC_age
from .CSEL.disturbances             import gaussZeta  as _DFLT_FUNC_zeta
from .CSEL.model_ddeint_firstOrder  import getEta     as _DFLT_FUNC_eta



class state:
	# constructor
	def __init__(self,inputs):
		### dependencies ###
		self.theInputs = inputs

		### constant (non-time-dependent) attributes (personality) ###
		self.name     = dataObject('name',nameSetter())
		self.birthday = dataObject('birthday',birthdaySetter(settings.simStartTime))

		self.personality = agentConstructor()

		### define dataObjects (potentially time-dependent) ###
		
		# sim-world age of agent
		self.age = dataObject('age',_DFLT_FUNC_age,self.birthday,settings.deltaTime,settings.simStartTime)

		## for physical activity (PA) ##
		# random distubances into the endogeneous flow vars, eta
		self.zeta_PA = dataObject('zeta_PA',_DFLT_FUNC_zeta)
		# array of endogeneous flow variables from package CSEL
		self.eta_PA  = dataObject('eta_PA',_DFLT_FUNC_eta,inputs.xi_PA,self.personality)

		## for eating behavior (EB) ##
		self.zeta_EB = dataObject('zeta_EB',_DFLT_FUNC_zeta)
		self.eta_EB  = dataObject('eta_EB',_DFLT_FUNC_eta,inputs.xi_EB,self.personality)
		

	# returns ALL data for given time t as a dict 
	def __call__(self,t):
		### return ALL info for that time as a dict ###
		return self.__dict__
		#return dict(name=self.name(t),\
		#            birthday=self.birthday(t),\
		#				personality=self.personality,\
		#				age     =self.age(t),\
		#            zeta_PA =self.zeta_PA(t),\
		#            eta_PA  =self.eta_PA(t),\
		#            zeta_EB =self.zeta_EB(t),\
		#            eta_EB  =self.eta_PA(t))


	# sets the personality of the agent using a new agent personality object 'newP'
	def setPersonality(self,newP):
		self.personality = newP
		# reset all personality-dependent data:
		self.eta_PA = dataObject('eta_PA',_DFLT_FUNC_eta,self.theInputs.xi_PA,newP)
		self.eta_EB = dataObject('eta_EB',_DFLT_FUNC_eta,self.theInputs.xi_EB,newP)

