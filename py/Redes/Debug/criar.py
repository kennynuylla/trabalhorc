import sys, networkx as nx, random as rnd
sys.path.append("/codigo/py/Comum")

import netlist

rede = nx.fast_gnp_random_graph(5, 0.8)

nós = rede.nodes(data=True)
arestas = rede.edges(data=True)

for nó in nós:
    nó[1]["importância"] = rnd.randint(0,10)

for aresta in arestas:
    aresta[2]["latência_efetiva"] = rnd.random()

netlist.GerarEdgeList(sys.argv[1], rede)
netlist.GerarNodeList(sys.argv[2], rede)