import numpy as np, matplotlib.pyplot as plt, networkx as nx, copy as cp


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

def simular_falha(rede, probabilidade):
    remover_nós_falha(rede, probabilidade)

    componentes_conectadas = nx.connected_components(rede)

    if(nx.number_connected_components(rede) == 0):
        return 0, 0
    
    maior_cluster = max(componentes_conectadas, key=(lambda item: encontrar_importância_componente(item,rede)))
    maior_cluster = rede.subgraph(maior_cluster).copy()

    return encontrar_importância_total(maior_cluster), encontrar_latência_efetiva_média(maior_cluster)

def gerar_pontos_resiliência(rede,b,x):
    importância_máxima = encontrar_importância_total(rede)
    latência_efetiva_máxima = encontrar_latência_efetiva_média(rede)

    probabilidades = np.linspace(0,1,x)
    importâncias = np.zeros(x)
    latências_efetivas = np.zeros(x)


    for n in range(b):
        for i in range(x):
            clone = cp.deepcopy(rede)
            importância, latência_efetiva_média = simular_falha(clone, probabilidades[i])
            importâncias[i] += importância
            latências_efetivas[i] += latência_efetiva_média

        print("Finalizando %d/%d" %(n+1, b))
    
    #Calcular Média
    importâncias /= b
    latências_efetivas /= b

    #Normalizar
    importâncias /= importância_máxima
    latências_efetivas /= latência_efetiva_máxima

    return importâncias, latências_efetivas, probabilidades






