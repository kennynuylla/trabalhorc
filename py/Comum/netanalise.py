import networkx as nx

def Analisar(rede):
    latência_efetiva_média = nx.average_shortest_path_length(rede, weight="latência_efetiva")
    importância_total = 0

    for nó in list(rede.nodes(data=True)):
        importância_total += nó[1]["importância_final"]

    return importância_total, latência_efetiva_média
    