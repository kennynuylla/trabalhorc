import numpy as np, matplotlib.pyplot as plt, networkx as nx, copy as cp, sys


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

def encontrar_maior_cluster(componentes, rede):
    importância = 0
    maior_cluster = None

    for componente in componentes:
        importância_componente = encontrar_importância_componente(componente, rede)
        if(importância_componente > importância):
            importância = importância_componente
            maior_cluster = componente

    return maior_cluster, importância

def analisar_componentes(rede):
    componentes_conectadas = nx.connected_components(rede)

    if(nx.number_connected_components(rede) == 0):
        return 0, 0
    
    maior_cluster, importância = encontrar_maior_cluster(componentes_conectadas, rede)
    maior_cluster = rede.subgraph(maior_cluster).copy()

    return importância, encontrar_latência_efetiva_média(maior_cluster)

def simular_falha(rede, probabilidade):
    remover_nós_falha(rede, probabilidade)
    return analisar_componentes(rede)


def simular_ataque(nós, rede, probabilidade):
    para_remover = []
    qtd_para_remover = int(np.round(probabilidade * len(nós)))
    for i in range(qtd_para_remover):
        para_remover.append(nós[i][0])

    rede.remove_nodes_from(para_remover)
    return analisar_componentes(rede)


def gerar_pontos_falha(rede, b,x):
    probabilidades = np.linspace(0,1,x)
    importâncias = np.zeros(x)
    latências_efetivas = np.zeros(x)

    print("Iniciando análise de falha")

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

    print("Análise de falha finalizada")

    return importâncias, latências_efetivas, probabilidades

def gerar_pontos_ataque(rede, b, x):
    probabilidades = np.linspace(0,1,x)
    importâncias = np.zeros(x)
    latências_efetivas = np.zeros(x)

    print("Iniciando análise de ataque")

    nós = list(rede.nodes(data=True))
    nós.sort(reverse=True, key = lambda item: item[1]["importância"] + rede.degree(item[0]))

    for n in range(b):
        for i in range(x):
            print("Começando probabilidade de remoção de %.2f (%d/%d)" %(probabilidades[i], i+1, x))
            clone = cp.deepcopy(rede)
            importância, latência_efetiva = simular_ataque(nós, clone, probabilidades[i])
            importâncias[i] += importância
            latências_efetivas[i] += latência_efetiva
            print("Finalizado probabilidade de remoção de %.2f (%d/%d)" %(probabilidades[i], i+1, x))

        print("Finalizando %d/%d" %(n+1, b))

    #Calcular Média
    importâncias /= b
    latências_efetivas /= b

    #Normalizar
    importâncias /= importâncias[0]
    latências_efetivas /= latências_efetivas[0]

    print("Análise de ataque finalizaada")

    return importâncias, latências_efetivas, probabilidades






