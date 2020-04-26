import sys, networkx as nx
from Bibliotecas import *

listaNós = sys.argv[1]
listaArestas = sys.argv[2]

rede = netlist.LerRede(listaNós, listaArestas)
componentes_conectadas = nx.connected_components(rede)

if(nx.number_connected_components(rede) == 0):
    netsaída.SairAnálise(0,0)

maior_cluster = max(componentes_conectadas, key=(lambda item: encontrar_importância_componente(item,rede)))
maior_cluster = rede.subgraph(maior_cluster).copy()