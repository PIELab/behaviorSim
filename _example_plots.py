import pylab

# === === === === === === AGENT SETUP === === === === === ===
import PECSagent.agent
agent1 = PECSagent.agent.agent()

# === === === === === === PLOTS === === === === === ===
#to make plots, we must get an array of the desired data:
timeArray = [agent1.inputs.time(t) for t in range(0,10)]
ageArray  = [agent1.state.age(t).total_seconds()/(60*60*24*365.242) for t in range(0,10)]

# then set up the figure:
pylab.figure('agent age[yrs] v time of subject born '+str(agent1.state.birthday))

# plot the data:
pylab.plot(timeArray,ageArray)
# force yticks to be in years (and not deci-years):
locs,labels = pylab.yticks()
pylab.yticks(locs, map(lambda ageArray: "%g" % ageArray, locs))
# and show the plot:
pylab.show()

