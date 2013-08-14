# this file defines a set of functions for creating information flow diagrams for the model

from ..__util.pydot import pydot
from PIL import Image

import logging

def getNodes(agent):
	return {'inputs':list(agent.inputs(0)),'state':list(agent.state(0)),'motive':list(agent.motive(0)),'behavior':list(agent.behavior(0))}

def getEdges(agent):
	nodeDict = getNodes(agent)
	for clusterName in list(nodeDict):
		for dataObjName in nodeDict[clusterName]:
			try: connArgs = eval('agent.inputs.'+dataObjName+'.args')
			except AttributeError:
				try: connArgs = eval('agent.state.'+dataObjName+'.args')
				except AttributeError:
					try: connArgs = eval('agent.motive.'+dataObjName+'.args')
					except AttributeError: 
						try: connArgs = eval('agent.behavior.'+dataObjName+'.args')
						except AttributeError: 
							logging.error('infoFlow.getEdges: attribute "'+dataObjName+'" cannot be found! check agent dicts against agent dataObject names.') 
							print 'ERR from infoFlow.getEdges: attribute "'+dataObjName+'" cannot be found! check agent dicts against agent dataObject names.'
							exit()
			for arg in connArgs:
				try: print '['+arg.name+', '+dataObjName+']'
				except AttributeError: print '[?, '+dataObjName+']'

def showInfoFlow(agent):
	graph = pydot.Dot(graph_type='digraph')

	nodeDict = getNodes(agent)
	#for each key in getNodes() dict
	for clustName in list(nodeDict):
		#create cluster
		cluster = pydot.Cluster(clustName,label=clustName)
		#add nodes to cluster
		for nodeName in nodeDict[clustName]:
			node = pydot.Node(nodeName)
			cluster.add_node(node)
		graph.add_subgraph(cluster)

	#TODO: add edges
	edgeList = getEdges(agent)

	# save the dot file
#	graph.write_raw('example_graph.dot')

	# create the graph image (using graphviz)
	graph.write_png('example_graph.png')

	# show the image
	im = Image.open('example_graph.png')
	im.show()

