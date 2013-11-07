# -*- coding: utf-8 -*-
"""
pydot test script
@author: Tylar Murray 
based on examples by [Federico Cáceres](http://pythonhaven.wordpress.com/2009/12/09/generating_graphs_with_pydot/)
and [Robert Yu](http://www.robertyu.com/wikiperdido/Pydot%20Clusters)
"""
import pydot
from PIL import Image

# in graph_type we specify we want a DIrected GRAPH
graph = pydot.Dot(graph_type='digraph')

# Use pydot.Cluster to render boundary around subgraph
cluster1=pydot.Cluster('cluster1',label='cluster1')

# creating nodes is as simple as creating edges!
node_a = pydot.Node("Node A", style="filled", fillcolor="red")
# but... what are all those extra stuff after "Node A"?
# well, these arguments define how the node is going to look on the graph, you can find a full reference here:
# http://www.graphviz.org/doc/info/attrs.html
# which in turn is part of the full docs in
# http://www.graphviz.org/Documentation.php

# create the rest of the nodes!
node_b = pydot.Node("Node B", style="filled", fillcolor="green")
node_c = pydot.Node("Node C", style="filled", fillcolor="#0000ff")
node_d = pydot.Node("Node D", style="filled", fillcolor="#976856")

# add the nodes to the cluster
cluster1.add_node(node_a)
cluster1.add_node(node_b)

# in order to get node in parent graph to point to
# subgraph, need to use Graph.add_subgraph()
# calling Subgraph.add_parent() doesn't seem to do anything.
graph.add_subgraph(cluster1)

# add other nodes (not in subgraph) to the graph
graph.add_node(node_d)
graph.add_node(node_c)

# create the edges
graph.add_edge(pydot.Edge(node_a, node_b))
graph.add_edge(pydot.Edge(node_b, node_c))
graph.add_edge(pydot.Edge(node_c, node_d))
# make this last edge special
graph.add_edge(pydot.Edge(node_d, node_a, label="and back we go again", labelfontcolor="#009933", fontsize="10.0", color="blue"))

# save the dot file
graph.write_raw('example_graph.dot')

# create the graph image (using graphviz)
graph.write_png('example_graph.png')

# show the image
im = Image.open('example_graph.png')
im.show()

