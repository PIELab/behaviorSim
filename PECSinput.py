timeToRun = 100;	#units are days (I think)

# === coefficients derived from structural equation modeling:
gamma = [[.11,   0,   0],\
	 [  0, .22,   0],\
	 [  0,   0, .33]];

beta  = [[  0,  0,  0,  0,  0],\
         [  0,  0,  0,  0,  0],\
         [  0,  0,  0,  0,  0],\
         [.41,.42,.43,  0,  0],\
         [  0,  0,.53,.54,  0]];

# ===
#init all to 0
belief = [0 for t in range(timeToRun)];
attitude = [0 for t in range(timeToRun)];
socialNorms = [0 for t in range(timeToRun)];
PBC = [0 for t in range(timeToRun)];
#set up inputs for all time values:
for t in range(timeToRun):
	if(t > 20):
		belief[t] = .8;
	else:
		belief[t] = .2;

	# === 'exogenous flow variables'from 2010 Navarro-Barrientos et al @ CSEL:
	#TODO: these inputs need to be set using eqtns 12-14
	attitude[t]   = belief[t] * .4;	#behavioralBeliefCrossEvaluation = 0;	#xi1; attitude towards behavior
	socialNorms[t]= .5;	#normativeCrossMotivation = 0;		#xi2; subjective norms
	PBC[t]        = .6;	#controlBeliefCrossPower = 0;		#xi3; perceived behavioral control


