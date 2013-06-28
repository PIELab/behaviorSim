# this file is used to run unit tests on various code bits

# setup logging
import logging
logging.basicConfig(filename='src/__logs/unitTesting.log',\
                    level=logging.DEBUG,\
                    format='%(asctime)s %(levelname)s:%(message)s')

def testAgentData():
	def littleCalcTest(d):
		print '   d.data='+str(d.data)
		print 'd.calc(1)='+str(d.calc(1))
		print '   d.data='+str(d.data)
		print '     d(2)='+str(d(2))
		print '   d.data='+str(d.data)
		print '   d(1.4)='+str(d(1.4))
		print '   d.data='+str(d.data)
		print '   d(1.5)='+str(d(1.5))
		print '   d.data='+str(d.data)
		print '   d(1.6)='+str(d(1.6))
		print '   d.data='+str(d.data)
		print '   d(5.6)='+str(d(5.6))
		print '   d.data='+str(d.data)

	print 'importing dataObject...'
	from src.__util.agentData import dataObject

	D = dataObject()
	print 'testing default setup...'
	littleCalcTest(D)
	
	print 'resetting dataObject...'
	D.reset()

	print 'testing customization...'
	D.setFunction(lambda t: t*10)
	littleCalcTest(D)
	

# ============================
# === === === MAIN === === ===
# ============================
testAgentData()

