from datetime import datetime	# for getTime

# getTime is a simple example to get the time. This function can be re-branded getInitTime() using from-import-as for easy implementation. 
# This function is time-invariant.
def getTime(self,t):
	if t < len(self.initTime):
		return self.initTime[t]
	else:
		now = datetime.now()
		for i in range(len(self.initTime),t+1):
			self.initTime.append(now)
	return self.initTime[t]
