import sys
from Bibliotecas import *

listaNós = sys.argv[1]
listaArestas = sys.argv[2]
caminhoArquivo = sys.argv[3]

rede = netlist.LerRede(listaNós, listaArestas)
netplot.PlotarRede(rede, caminhoArquivo)
