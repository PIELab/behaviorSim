PECSmodeler
===========

A toolkit for agent-based modeling of human systems. This framework is designed to be theory-independent, extensible, and very easy to use. 

We are actively searching for collaborators and users of this toolkit! If you want to use this toolkit to perform simulations, implement a cognitive/behavioral theory, or test out add your machine-learning model to our collection please contact me (tylarmurray@mail.usf.edu) and I will be thrilled to help you. You may also find more information in the [wiki page](https://github.com/7yl4r/PECSmodeler/wiki).

Basic Setup
-------------------------
This is not the only way to install, but we're going to walk you through the easiest way.
### General Steps ###
1. [install python 2.7 (other versions *might* work)](http://www.python.org/download/)
2. [install git](http://git-scm.com/book/en/Getting-Started-Installing-Git)
3. download & install pylab & dependencies
4. download behaviorSim using git
5. cd into behaviorSim directory & start behaviorSimUI.py

### For Ubuntu ###
1. open a terminal (ctrl+alt+t)
2. install python `sudo apt-get install python`
3. install pylab `sudo apt-get install python-numpy python-scipy python-matplotlib`
4. install git `sudo apt-get install git`
5. download behaviorSim source code `git clone https://github.com/PIELab/behaviorSim.git`
6. enter behaviorSim directory `cd behaviorSim`
7. start behaviorSim main UI `python behaviorSimUI.py`

### For Windows ###
1. [download & install Enthought Canopy version of python 2.7](https://www.enthought.com/downloads/) (NOTE: [python(x,y)](https://code.google.com/p/pythonxy/wiki/Downloads?tm=2) may be a valid alternative.)
2. [download & install git](http://git-scm.com/download/win)
3. open git bash command prompt
4. enter `cd Documents` to enter your documents directory
5. enter `git clone https://github.com/PIELab/behaviorSim.git` to download behaviorSim source code
6. open canopy command prompt window
6. enter `cd Documents/behaviorSim` to enter behaviorSim directory 
7. start behaviorSim main UI by typing `python behaviorSimUI.py` (or `C:\Python27\python.exe behaviorSimUI.py`)

additional troubleshooting stuff:
* test python install by checking version. Type `python -V` in command prompt; if this does not work try something like `C:\Python27\python.exe -V`.

these instructions used to be included, but don't really work:
5. enter `git clone git@github.com:matplotlib/matplotlib.git` in cmd prompt to download matplotlib
6. enter `cd matplotlib` in cmd propmt to enter matplotlib directory
7. enter `python setup.py install` (or `C:\Python27\python.exe setup.py install`) to install

### Mac OS ###
???

### Other Linux ###
???

Advanced Setup
-------------------
If you are trying to use some more advanced features of the software, you may need to do some more setup.

### Feature-dependent dependencies ###
The following modules are required to use certain features, but the core software can be run without them.
* The horizonGraph plotter requires an install of the matplotlib add-on from [thomaskern/horizongraph_matplotlib](https://github.com/thomaskern/horizongraph_matplotlib).
* viewing informationFlow graphs using requires [graphViz](http://www.graphviz.org/). Simply install with "sudo apt-get graphviz".

### Included Packages ###
The following dependencies are packaged into the behaviorSim.__util directory and no setup or worry about them is needed, but they help make this work possible and merit mention here:
* [pydot](https://code.google.com/p/pydot/) for creating informationFlow graphs
* [ddeint](http://zulko.wordpress.com/2013/03/01/delay-differential-equations-easy-with-python/) for solving delay differential equations
* [appdirs](https://pypi.python.org/pypi/appdirs/1.2.0) - "A small Python module for determining appropriate platform-specific dirs". Used under permission of the [MIT License](http://opensource.org/licenses/MIT).

Package Structure
-----------------
If you would like to add functions or data objects to the agent, it is best to keep them nested in their proper location in following package structure. Please try to refrain from changing the existing data objects and only add if absolutely necessary. If you are going to add a piece of information to one of the components, use the dataObject() class in __util/agentData.py. The idea here is to build up a complete data structure for behavior modeling and allow the functions associated with each piece of information to be swapped out easily.
		myScript.py (run any scripts or start python here)
		src/
			PECSagent/
				agent.py
				settings.py
				inputs/
					inputs.py
					(implementation packages here)
				state/
					state.py
					(implementation packages here)
				motive/
					motive.py
					(implementation packages here)
				output/
					output.py
					(implementation packages here)

Components
-----------
The agent model is split into the following components in an attempt to make flow of information through the agent more organized. Please see [the wiki page on information flow](https://github.com/PIELab/behaviorSim/wiki/information-flow) for more information, and consider the following descriptions of model components.
### Inputs ###
Inputs represent the context of the agent. This input comes from the environment exterior to the agent or from past actions of the agent.

### State ###
This component represents the internal state of the agent. All information here should be a property of the agent. These states are separated into the four componenents which give the PECS model its name: Physical, Emotional, Cognitive, and Social.

### Motive ###
The motives of an agent are analagous to the 'dependent variables' of the PECS reference model, and represent the motivations, drives, and intentions of the agent.

### Output ###
The output of the agent shows the agent's behavior as determined from motives, states, and inputs.

Adding to the Model
--------------------
The PECS model framework is designed to be extended to allow for the exploration of many behavior models. The following steps should be take to add to the model:
> 1. *Add your package to the applicable component.* 
> For instance, a new input definition, your package should be added to PECSagent/Inputs/. 
> 2. *Adjust component definition.* 
> The contents of the default component definition should be adjusted to use your new package or to add your new variables. For example: if you intend to add a new state variable, you must add the variable to PECSagent/state/state.py. If you are just changing the way an existing state variable is calculated, you can just change the import statement at the top of the file or load your custom function in a script.
>*NOTE*: only add to the component definitions; never remove variables. Ideally, your package can use existing variables but all state variables are not yet incorporated. Please add variables with caution and use descriptive names to enable re-use by other packages.
