# this file is used to run unit tests on various code bits

def testAgentData():
	def littleCalcTest(d):
		print '   d.data='+str(d.data)
		print 'd.calc(1)='+str(d.calc(1))
		print '   d.data='+str(d.data)
		print '     d(2)='+str(d(2))
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

