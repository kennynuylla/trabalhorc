import networkx as nx 
import sys

rede = nx.fast_gnp_random_graph(5, 0.8)
nx.write_weighted_edgelist(rede, "%s" %(sys.argv[1]))