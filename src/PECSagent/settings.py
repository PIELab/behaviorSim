# this class defines the global settings for the simulation

from datetime import datetime, timedelta
import logging

class settings:
	deltaTime    = timedelta(days=1)	# sim-world time between steps
	simStartTime = datetime(2013, 5, 30, 11, 17, 0, 0) # sim-time of the beginning of the simulation NOTE: all agents are assumed to be in the same time zone so no tzinfo is included here.
	subSteps     = 100	# used for integrations; when a continuous function is specified, how many subSteps per deltaTime are computed? MUST be even?!?

	# this sets up a log config if one hasn't been set yet. If one is set previously, this one is ignored.
	logging.basicConfig(filename='src/__logs/defaultLogFile.log',\
		                 level=logging.WARNING,\
		                format='%(asctime)s %(levelname)s:%(message)s')
