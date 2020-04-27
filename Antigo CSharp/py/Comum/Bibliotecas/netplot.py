import matplotlib.pyplot as plt, networkx as nx

def PlotarRede(rede, caminhoPlot):
    plt.figure(figsize=(12,12), dpi=128)
    labels = nx.get_node_attributes(rede, "importância")
    nx.draw(rede, labels=labels, node_size=1000, font_size=20)
    plt.savefig(caminhoPlot)
    plt.close()