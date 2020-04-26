import sys, networkx as nx, random as rnd
sys.path.append("/codigo/py/Comum")
from Bibliotecas import *

rede = nx.fast_gnp_random_graph(7, 0.8)

nós = rede.nodes(data=True)
arestas = rede.edges(data=True)

listaNós = sys.argv[1]
listaArestas = sys.argv[2]

for nó in nós:
    nó[1]["importância"] = rnd.randint(0,10)

for aresta in arestas:
    aresta[2]["latência_efetiva"] = rnd.random()

netlist.GerarEdgeList(listaArestas, rede)
netlist.GerarNodeList(listaNós, rede)

i,l = netanalise.Analisar(rede)
netsaída.SairAnálise(i,l)