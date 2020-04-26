import sys, networkx as nx, random as rnd
from Bibliotecas import *

listaNós = sys.argv[1]
listaArestas = sys.argv[2]
probabilidaRemoção = float(sys.argv[3])

rede = netlist.LerRede(listaNós, listaArestas)

nósRemover = []

for nó in rede.nodes:
    if(rnd.random() <= probabilidaRemoção):
        nósRemover.append(nó)

rede.remove_nodes_from(nósRemover)

importância_total, latência = netanalise.AnalisarComponentes(rede)
netsaída.SairAnálise(importância_total, latência)
