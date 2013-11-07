"""
Run this script to start main behaviorSim user-interface.
"""

from behaviorSim.interface import CLI
from behaviorSim.globals import *

print """
=== behaviorSim v"""+VERSION+""" ===
for support contact USF PIE-Lab at
"""+CONTACT_EMAIL+""" 
==============================

"""

CLI.promptForScriptOrSample()
print 'goodbye.'

