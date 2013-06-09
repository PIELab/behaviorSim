# gets a name from a list
# method metadata:
	# time-invariant? = TRUE
	# (sim)time-dependent? = TRUE
# requirements for this method to be valid:
	# requiredTimeScale = null
	# requiredTimeStep  = null
nameList = ['Alice','Bob','Charles','Dr. Farnsworth','Eugene']	#TODO: add more names
n        = 0
def iterativeNamer():
	global n, nameList
	if n > len(nameList)-1:
		n = 0
	name = nameList[n]
	n += 1
	return name

