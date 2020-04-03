import sys, os
sys.path.append("./Estruturas de Dados")
sys.path.append("./Grafos")
sys.path.append("./Exceptions")
sys.path.append("./Bibliotecas")
sys.path.append("./DAO")


import Aleatório as grafo


if not(os.path.exists("Saída")):
    os.mkdir("Saída")

quantidade_nós = int(sys.argv[1])
quantidade_repetições = int(sys.argv[2])
quantidade_probabilidades = int(sys.argv[3])

rede = grafo.Aleatório()
rede.montar(quantidade_nós)
print("Rede Montada")
#rede.desenhar()
#print("Rede Desenhada")
rede.analisar(quantidade_repetições, quantidade_probabilidades)
print("Rede Analisada")
rede.gerar_gráficos_resiliência()