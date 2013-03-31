# represents an agent state at one moment in time
class agentState:
	attitude    = 0;	#eta1
	socialNorms = 0;	#eta2
	PBC         = 0;	#eta3
	intention   = 0;	#eta4
	behavior    = 0;	#eta5

	def __init__(self,modelInput):
		#'endogeneous flow variables' from 2010 Navarro-Barrientos et al @ CSEL:
		self.attitude    = modelInput.gamma[0,0]*modelInput.xi[0,0];	#eta1; attitude towards behavior
		self.socialNorms = modelInput.gamma[1,1]*modelInput.xi[1,0];	#eta2; subjective norms
		self.PBC         = modelInput.gamma[2,2]*modelInput.xi[2,0];	#eta3; perceived Behavioral Control
		self.intention   = modelInput.beta[3,0]*self.attitude \
		                 + modelInput.beta[3,1]*self.socialNorms + modelInput.beta[3,2]*self.PBC;
		self.behavior    = modelInput.beta[4,3]*self.intention   + modelInput.beta[4,2]*self.PBC;

	# sets all state vars to those in the given state
	def setState(self, newState):
		self.attitude    = newState.attitude;
		self.socialNorms = newState.socialNorms;
		self.PBC         = newState.PBC;		
		self.intention   = newState.intention;		
		self.behavior    = newState.behavior;		
		
