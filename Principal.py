import sys, os, argparse
sys.path.append("./Estruturas de Dados")
sys.path.append("./Grafos")
sys.path.append("./Exceptions")
sys.path.append("./Bibliotecas")
sys.path.append("./DAO")

parser = argparse.ArgumentParser()
parser.add_argument("--qtdnos", help="Quantidade de Nós", type=int)
parser.add_argument("--rep", help="Quantidade de Repetições", type=int)
parser.add_argument("--prob", help="Quantidade de Probabilidades", type=int)
args = parser.parse_args()

import Aleatório as grafo


if not(os.path.exists("Saída")):
    os.mkdir("Saída")

quantidade_nós = args.qtdnos if args.qtdnos else 100
quantidade_repetições = args.rep if args.rep else 1
quantidade_probabilidades = args.prob if args.prob else 100

rede = grafo.Aleatório()
rede.montar(quantidade_nós)
print("Rede Montada")
#rede.desenhar()
#print("Rede Desenhada")
rede.analisar(quantidade_repetições, quantidade_probabilidades)
print("Rede Analisada")
rede.gerar_gráficos_resiliência()