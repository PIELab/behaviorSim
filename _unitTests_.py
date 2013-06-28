# this file is used to run unit tests on various code bits

def testAgentData():
	from src.__util.agentData import dataObject
	d = dataObject()
	print '   d.data='+str(d.data)
	print 'd.calc(1)='+str(d.calc(1))
	print '   d.data='+str(d.data)
	print '     d(2)='+str(d(2))
	print '   d.data='+str(d.data)

testAgentData()

