from firstOrderInput import * 

class agentState:
	#'endogeneous flow variables' from 2010 Navarro-Barrientos et al @ CSEL:
	attitude    = gamma[0,0]*xi[0,0];	#eta1; attitude towards behavior
	socialNorms = gamma[1,1]*xi[1,0];	#eta2; subjective norms
	PBC         = gamma[2,2]*xi[2,0];	#eta3; perceived Behavioral Control
	intention   = beta[3,0]*attitude + beta[3,1]*socialNorms + beta[3,2]*PBC;		#eta4;
	behavior    = beta[4,3]*intention + beta[4,2]*PBC;		#eta5;

	# sets all state vars to those in the given state
	def setState(self, newState):
		self.attitude    = newState.attitude;
		self.socialNorms = newState.socialNorms;
		self.PBC         = newState.PBC;		
		self.intention   = newState.intention;		
		self.behavior    = newState.behavior;		
		
