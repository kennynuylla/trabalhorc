import sys, netlist, netplot

rede = netlist.LerRede(sys.argv[1], sys.argv[2])
netplot.PlotarRede(rede, sys.argv[3])
