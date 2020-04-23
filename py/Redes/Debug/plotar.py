import sys, networkx as nx
sys.path.append("/codigo/py/Comum")

import netlist
import netplot

rede = netlist.LerRede(sys.argv[1], sys.argv[2])
netplot.PlotarRede(rede, sys.argv[3])
