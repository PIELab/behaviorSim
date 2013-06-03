PECSmodeler
===========

An implementation of the PECS (physis, emotion, cognition, social) agent model. 

Package Structure
-----------
		PECSmodeler/
			myScript.py (run any scripts or start python here)
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
### Inputs ###
Inputs represent the context of the agent. This input comes from the environment exterior to the agent or from past actions of the agent.

### State ###
This component represents the internal state of the agent. All information here should be a property of the agent. These states are separated into the four componenents which give the PECS model its name: Physical, Emotional, Cognitive, and Social.

### Motive ###
The motives of an agent are analagous to the 'dependent variables' of the PECS reference model, and represent the motivations, drives, and intentions of the agent.

### Output ###
The output of the agent shows the agent's behavior as determined from motives, states, and inputs.
