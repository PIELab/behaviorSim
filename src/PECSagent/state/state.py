# the state class encapsulates all information pertaining to the internal state variables of the agent

from ..settings import settings
from ...__util.agentData import dataObject

import logging

### import personality setters ###
from .baseInfo.age  import randomAger     as birthdaySetter
from .baseInfo.name import iterativeNamer as nameSetter

from .CSEL.agent_defaultPersonality import agent      as agentConstructor

### import default functions for data ###
from .baseInfo.age                  import age        as _DFLT_FUNC_age
from .CSEL.disturbances             import gaussZeta  as _DFLT_FUNC_zeta
from .CSEL.model_ddeint_firstOrder  import getEta     as _DFLT_FUNC_eta



class state:	#can't use 'input' as the name b/c of built-in 'input()'
	# constructor
	def __init__(self,inputs):
		### dependencies ###
		self.theInputs = inputs

		### constant (non-time-dependent) attributes (personality) ###
		self.name     = nameSetter()
		self.birthday = birthdaySetter(settings.simStartTime)

		self.agentPersonality = agentConstructor()

		### define dataObjects (potentially time-dependent) ###
		
		# sim-world age of agent
		self.age = dataObject(_DFLT_FUNC_age,self.birthday,settings.deltaTime,settings.simStartTime)

		# random distubances into the endogeneous flow vars, eta
		self.zeta = dataObject(_DFLT_FUNC_zeta)

		# array of endogeneous flow variables from package CSEL
		self.eta  = dataObject(_DFLT_FUNC_eta,inputs.xi,self.agentPersonality)
		

	# returns ALL data for given time t as a dict 
	def __call__(self,t):
		### return ALL info for that time as a dict ###
		return dict(agentName=self.name,\
		            birthday=self.birthday,\
		            age     =self.age(t))

	# sets the personality of the agent using a new agent personality object 'newP'
	def setPersonality(self,newP):
		self.agentPersonality = newP
		# reset all personality-dependent data:
		self.eta = dataObject(_DFLT_FUNC_eta,self.theInputs.xi,newP)

