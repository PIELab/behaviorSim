# this class defines the global settings for the simulation

from datetime import datetime, timedelta

class settings:
	deltaTime    = timedelta(days=1)	# sim-world time between steps
	simStartTime = datetime(2013, 5, 30, 11, 17, 0, 0) # sim-time of the beginning of the simulation NOTE: all agents are assumed to be in the same time zone so no tzinfo is included here.
	subSteps     = 20	# used for integrations; when a continuous function is specified, how many subSteps per deltaTime are computed?
