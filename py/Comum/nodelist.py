def gerarNodeList(arquivo, lista):
    arquivo = open(arquivo, "w")

    for nó in lista:
        arquivo.write("%s %s\n" %(nó[0], nó[1]))

    arquivo.close()