import sys, networkx as nx 
sys.path.append("/codigo/py/Comum")

import nodelist as ndlist

rede = nx.fast_gnp_random_graph(5, 0.8)
nx.write_weighted_edgelist(rede, "%s" %(sys.argv[1]))
ndlist.gerarNodeList(sys.argv[2], list(rede.nodes(data=True)))