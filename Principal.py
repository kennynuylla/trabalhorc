import sys
sys.path.append("./Estruturas de Dados")
sys.path.append("./Grafos")
sys.path.append("./Exceptions")
sys.path.append("./Bibliotecas")
sys.path.append("./DAO")


import Aleatório as grafo


rede = grafo.Aleatório()
rede.montar()
print("Rede Montada")
#rede.desenhar()
#print("Rede Desenhada")
rede.analisar()
print("Rede Analisada")
rede.gerar_gráficos_resiliência()