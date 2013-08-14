# this file defines a set of functions for creating information flow diagrams for the model

from ..__util.pydot import pydot
from PIL import Image

import logging

def getNodes(agent):
	return {'inputs':list(agent.inputs(0)),'state':list(agent.state(0)),'motive':list(agent.motive(0)),'behavior':list(agent.behavior(0))}

def getEdges(agent):
	edgeList = list()
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
							logging.error('infoFlow.getEdges: attribute "'+dataObjName+\
							   '" from agent dict cannot be found! check against agent dataObject names.') 
							print '\nERR from infoFlow.getEdges: attribute "'+dataObjName+\
							   '" cannot be found! check agent dicts against agent dataObject names.'
			for arg in connArgs:
				try: 
					edgeList.append([arg.name,dataObjName])
					#print '['+arg.name+', '+dataObjName+']' 
				except AttributeError: print '\nERR: for edge [?, '+dataObjName+'] ("name" attribute not found)'
	return edgeList
	
def showInfoFlow(agent):
	graph = pydot.Dot(graph_type='digraph')

	#add environment node(s) at start & end
	graph.add_node(pydot.Node('environment'))

	nodeDict = getNodes(agent)
	#for each key in getNodes() dict
	for clustName in list(nodeDict):
		#create cluster
		cluster = pydot.Cluster(clustName,label=clustName)
		#add nodes to cluster
		for nodeName in nodeDict[clustName]:
			node = pydot.Node(nodeName)
			cluster.add_node(node)
			# print 'node added'
		graph.add_subgraph(cluster)
		# print 'subgraph added'

	def getNodeFromSubGraphs(graph,name):
		nodeL = list()
		for subG in graph.get_subgraphs():
			#print subG.get_nodes()
			n = subG.get_node(name)
			if len(n) == 1:
				nodeL.append(n[0])
			elif len(n) > 1:
				nodeL.append(n)
		if len(nodeL)==1:
			return nodeL[0]
		else: return nodeL
		

	#TODO: add edges
	edgeList = getEdges(agent)
	for edge in edgeList:
		n1 = getNodeFromSubGraphs(graph,edge[0])
		n2 = getNodeFromSubGraphs(graph,edge[1])
		#print edge[0]+'--->'+edge[1]
		#print str(n1)+'--->'+str(n2)
		ed = pydot.Edge(n1, n2)
		try: graph.add_edge(ed)
		except TypeError: print '\nERR: cannot find one or more nodes for edge '+str(edge)+'\n\tn1='+str(n1)+'\n\tn2='+str(n2)

	# save the dot file
#	graph.write_raw('example_graph.dot')

	# create the graph image (using graphviz)
	graph.write_png('example_graph.png')

	# show the image
	im = Image.open('example_graph.png')
	im.show()

