import networkx as nx

def Analisar(rede):
    latência_efetiva_média = CalcularLatência(rede)
    importância_total = 0

    for nó in list(rede.nodes(data=True)):
        importância_total += nó[1]["importância"] + rede.degree(nó[0])

    return importância_total, latência_efetiva_média

def CalcularLatência(rede):
    return nx.average_shortest_path_length(rede, weight="latência_efetiva")
    