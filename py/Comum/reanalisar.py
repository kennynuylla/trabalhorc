import sys, networkx as nx
from Bibliotecas import *

listaNós = sys.argv[1]
listaArestas = sys.argv[2]

rede = netlist.LerRede(listaNós, listaArestas)
componentes_conectadas = nx.connected_components(rede)

if(nx.number_connected_components(rede) == 0):
    netsaída.SairAnálise(0,0.00)
    sys.exit(0)

importância_total = 0
nós = rede.nodes(data=True)
maior_componente = None

for componente in componentes_conectadas:
    importância_componente = 0
    for nó in componente:
        importância_componente += nós[nó]["importância"] + rede.degree(nó)

    if(importância_componente > importância_total):
        importância_total = importância_componente
        maior_componente = componente

maior_cluster = rede.subgraph(maior_componente)
netsaída.SairAnálise(importância_total, netanalise.CalcularLatência(maior_cluster))