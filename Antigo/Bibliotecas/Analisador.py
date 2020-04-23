import numpy as np, matplotlib.pyplot as plt, networkx as nx, copy as cp


def encontrar_importância_total(rede):
    nós = rede.nodes(data=True)
    k = 0
    for nó in nós:
        k += nó[1]["importância"] + rede.degree[nó[0]]

    return k

def encontrar_importância_componente(componente,rede):
    k = 0
    nós_rede = rede.nodes(data=True)
    for nó in componente:
        k += nós_rede[nó]["importância"] + rede.degree[nó]
    return k

def encontrar_latência_efetiva_média(rede):
    return nx.average_shortest_path_length(rede, weight="latência_efetiva")

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

def gerar_pontos_resiliência(rede, b,x):
    probabilidades = np.linspace(0,1,x)
    importâncias = np.zeros(x)
    latências_efetivas = np.zeros(x)


    for n in range(b):
        for i in range(x):
            print("Começando probabilidade de remoção de %.2f (%d/%d)" %(probabilidades[i], i+1, x))
            clone = cp.deepcopy(rede)
            importância, latência_efetiva_média = simular_falha(clone, probabilidades[i])
            importâncias[i] += importância
            latências_efetivas[i] += latência_efetiva_média
            print("Finalizado probabilidade de remoção de %.2f (%d/%d)" %(probabilidades[i], i+1, x))

        print("Finalizando %d/%d" %(n+1, b))
    
    #Calcular Média
    importâncias /= b
    latências_efetivas /= b

    #Normalizar
    importâncias /= importâncias[0]
    latências_efetivas /= latências_efetivas[0]

    return importâncias, latências_efetivas, probabilidades






