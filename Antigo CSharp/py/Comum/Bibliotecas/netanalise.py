import networkx as nx

def Analisar(rede):
    latência_efetiva_média = CalcularLatência(rede)
    importância_total = 0

    for nó in list(rede.nodes(data=True)):
        importância_total += nó[1]["importância"] + rede.degree(nó[0])

    return importância_total, latência_efetiva_média

def CalcularLatência(rede):
    return nx.average_shortest_path_length(rede, weight="latência_efetiva")
    
def AnalisarComponentes(rede):
    componentes_conectadas = nx.connected_components(rede)

    if(nx.number_connected_components(rede) == 0):
        return 0,0.00

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
    
    return importância_total, CalcularLatência(maior_cluster)