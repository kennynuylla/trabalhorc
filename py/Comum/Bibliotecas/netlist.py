import networkx as nx

def GerarNodeList(localArquivo, rede):
    arquivo = open(localArquivo, "w")
    nós = list(rede.nodes(data=True))

    for nó in nós:
        arquivo.write("%s %d\n" %(nó[0], nó[1]["importância"]))

    arquivo.close()

def GerarEdgeList(localArquivo, rede):
    arquivo = open(localArquivo, "w")
    arestas = list(rede.edges(data=True))

    for aresta in arestas:
        arquivo.write("%s %s %f\n" %(aresta[0], aresta[1], aresta[2]["latência_efetiva"]))

    arquivo.close()

def LerRede(localArquivoNós, localArquivoArestas):
    rede = nx.Graph()
    InserirNodeList(localArquivoNós, rede)
    InserirEdgeList(localArquivoArestas, rede)

    return rede

def InserirNodeList(localArquivo, rede):
    arquivo = open(localArquivo, "r")
    linhas = arquivo.readlines()
    arquivo.close()

    for linha in linhas:
        linha = linha.strip()
        linha = linha.split(" ")
        rede.add_node(linha[0], importância=int(linha[1]))

def InserirEdgeList(localArquivo, rede):
    arquivo = open(localArquivo, "r")
    linhas = arquivo.readlines()
    arquivo.close()

    for linha in linhas:
        linha = linha.strip()
        linha = linha.split(" ")
        rede.add_edge(linha[0], linha[1], latência_efetiva=float(linha[2]))