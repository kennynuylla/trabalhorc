import sys, networkx as nx
from Bibliotecas import *

listaNós = sys.argv[1]
listaArestas = sys.argv[2]

rede = netlist.LerRede(listaNós, listaArestas)
importância_total, latência = netanalise.AnalisarComponentes(rede)
netsaída.SairAnálise(importância_total, latência)