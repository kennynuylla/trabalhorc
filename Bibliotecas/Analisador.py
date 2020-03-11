import numpy as np, matplotlib.pyplot as plt, networkx as nx


def encontrar_importância_total(rede):
    nós = rede.nodes(data=True)
    k = 0
    for nó in nós:
        k += nó[1]["importância"]

    return k

def encontrar_importância_componente(componente,rede):
    k = 0
    nós_rede = rede.nodes(data=True)
    for nó in componente:
        k += nós_rede[nó]["importância"]
    return k

def encontrar_latência_efetiva_média(rede):
    arestas = rede.edges(data=True)
    d = 0

    if(len(arestas) == 0):
        return 0

    for aresta in arestas:
        latência = aresta[2]["latência"]
        taxa_transmissão_média = aresta[2]["transmissão_média"]
        taxa_transmissão_máxima = aresta[2]["transmissão_máxima"]
        d += latência/(1 - taxa_transmissão_média/taxa_transmissão_máxima)

    return d/len(arestas)

def remover_nós_falha(rede, probabilidade):
    nós = rede.nodes()
    para_deletar = []
    for nó in nós:
        if(np.random.rand() < probabilidade):
            para_deletar.append(nó)

        

    rede.remove_nodes_from(para_deletar)

def gerar_pontos_resiliência(rede,b,x):
    importância_máxima = encontrar_importância_total(rede)
    latência_efetiva_máxima = encontrar_latência_efetiva_média(rede)

    probabilidades = np.linspace(0,1,x)
    importâncias = np.zeros(x)
    latências_efetivas = np.zeros(x)

    remover_nós_falha(rede, 0.3)

    plt.figure(figsize=(16,16), dpi=256)
    nx.draw(rede, with_labels=True, font_weight='bold')
    plt.savefig("./Saída/grafo.png")

    componentes_conectadas = nx.connected_components(rede)
    maior_cluster = max(componentes_conectadas, key=(lambda item: encontrar_importância_componente(item,rede)))
    maior_cluster = rede.subgraph(maior_cluster).copy()
    print(encontrar_importância_total(maior_cluster))
    print(encontrar_latência_efetiva_média(maior_cluster))




