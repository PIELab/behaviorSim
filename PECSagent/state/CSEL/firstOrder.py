from datetime import datetime
import random 

# gets the sim-world age of an agent given birth-datetime and simulation deltaT
# method metadata:
	# time-invariant? = TRUE
	# (sim)time-dependent? = TRUE
# requirements for this method to be valid:
	# requiredTimeScale = null
	# requiredTimeStep  = null
def age(data,t,birthdatetime,deltaT,t0):
	if t < len(data):
		return data[t]
	else:	# fill in data up to t
		if t == 0:
			ageAtStart = t0 - birthdatetime
			data.append(ageAtStart)
		for i in range(len(data),t+1):
			age = data[i-1] + deltaT
			data.append(age)
	return data[t]

# returns a randomly chosen age based on a flat (TODO: make this normal) probability distribution to make the average age at currentTime reasonable
def randomAger(currentTime):
	minYearAge = 5
	maxYearAge = 70
	yrAge = random.randint(minYearAge,maxYearAge)	#years of age

	y = currentTime.year - yrAge
	m = random.randint(1,12)	#birthmonth
	d = random.randint(1,28)	#birthday - nobody is ever born in the later days (TODO: fix this)
	h = random.randint(0,23)	#birthhour
	mn= random.randint(0,59)	#birthmin
	s = random.randint(0,59)	#birthsec
	return datetime(y,m,d,h,mn,s)
	
