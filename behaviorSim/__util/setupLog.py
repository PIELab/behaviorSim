		#NOTE: this file only resets when golly is restarted, 
		#      otherwise the log object is retained and reused, 
		#      appending to the file as the script is run multiple times
from os.path import expanduser,join
from os import makedirs
import logging

from .appdirs import user_log_dir

def setupLog(logName='log.txt'):
	logDir = user_log_dir('behaviorSim','PIE-Lab')
	try:
		makedirs(logDir)
	except OSError:
		pass # probably the dir already exists...
	logPath = join(logDir,logName)
	logging.basicConfig(filename=logPath,\
						level=logging.DEBUG,\
						format='%(asctime)s %(levelname)s:%(message)s',\
						filemode='w')   



#		# assume that you want your logs in LifeGenes source which is in your home directory
#		# (this works best on my linux machine)
#		home = expanduser("~")
#		logDir = home+'/LifeGenes/__logs'
#		try:
#			mkdir(logDir)
#		except OSError:
#			pass # probably the dir already exists...
#		
#		logPath = logDir+'/'+logName
#		print str(logging.getLogger())
#		logging.basicConfig(filename=logPath,\
#							level=logging.DEBUG,\
#							format='%(asctime)s %(levelname)s:%(message)s',\
#							filemode='w')
	try:
		print 'created .log at '+str(logPath)
	except:
		logging.warn('cannot print to stdout')