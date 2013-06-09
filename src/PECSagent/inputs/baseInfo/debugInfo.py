from datetime import datetime	# for getTime

# simple example to get the real-world time.
# method metadata:
	# time-invariant? = TRUE
	# (sim)time-dependent? = FALSE
# requirements for this method to be valid:
	# requiredTimeScale = null
	# requiredTimeStep  = null
def currentTime(data,t):
	if t < len(data):
		return data[t]
	else:	# fill in data up to t
		now = datetime.now()
		for i in range(len(data),t+1):
			data.append(now)
	return data[t]

# the most basic of testing functions, this returns the index that is given
# method metadata:
	# time-invariant? = TRUE
	# (sim)time-dependent? = TRUE
# requirements for this method to be valid:
	# requiredTimeScale = null
	# requiredTimeStep  = null
def pointless(data,index):
	if index < len(data):
		return data[index]
	else: # fill in data up to t
		for i in range(len(data),index+1):
			data.append(i)
	# now data[index] == index 
	return data[index]

