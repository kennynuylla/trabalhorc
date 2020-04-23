def gerarNodeList(arquivo, rede):
    arquivo = open(arquivo, "w")
    nós = rede.nodes(data=True)
    lista = list(nós)

    for nó in lista:
        arquivo.write("%s %d %d\n" %(nó[0], nó[1]["importância"], rede.degree(nó[0])))

    arquivo.close()