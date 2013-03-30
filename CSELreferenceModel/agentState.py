class agentState:
	#'endogeneous flow variables' from 2010 Navarro-Barrientos et al @ CSEL:
	attitude = 0;		#eta1; attitude towards behavior
	socialNorms = 0;	#eta2; subjective norms
	PBC = 0;		#eta3; perceived Behavioral Control
	intention = 0;		#eta4;
	behavior = 0;		#eta5;

	#TODO: inlude something like 'def init(self, initState)' to initialize all state vars to given state
	def setState(self, newState):
		self.attitude    = newState.attitude;
		self.socialNorms = newState.socialNorms;
		self.PBC         = newState.PBC;		
		self.intention   = newState.intention;		
		self.behavior    = newState.behavior;		
		
