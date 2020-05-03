import sys, os, argparse
sys.path.append("./Estruturas de Dados")
sys.path.append("./Grafos")
sys.path.append("./Exceptions")
sys.path.append("./Bibliotecas")
sys.path.append("./DAO")

parser = argparse.ArgumentParser()
parser.add_argument("--qtdnos", help="Quantidade de Nós (padrão: 100)", type=int)
parser.add_argument("--rep", help="Quantidade de Repetições (padrão: 1)", type=int)
parser.add_argument("--prob", help="Quantidade de Probabilidades (padrão: 100)", type=int)
parser.add_argument("--taxa", help="Taxa de Conexão (padrão: 0.8; Vale apenas para G(n,p))", type=float)
parser.add_argument("--tipo", help="gnp para G(n,p) e livre para Livre de Escala (padrão: gnp)")
args = parser.parse_args()

import Aleatório as grafo


if not(os.path.exists("Saída")):
    os.mkdir("Saída")

tipo = args.tipo if args.tipo else "gnp"
quantidade_nós = args.qtdnos if args.qtdnos else 100
quantidade_repetições = args.rep if args.rep else 1
quantidade_probabilidades = args.prob if args.prob else 100
taxa_conexão = args.taxa if args.taxa else 0.8

rede = grafo.Aleatório()
rede.montar(tipo, quantidade_nós, taxa_conexão)
print("Rede Montada")
rede.analisar(quantidade_repetições, quantidade_probabilidades)
print("Rede Analisada")
rede.exportarCSV()
#rede.gerar_gráficos_resiliência()