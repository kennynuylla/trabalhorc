from abc import ABC, abstractmethod
import networkx as nx, matplotlib.pyplot as plt, Constantes, pandas as pd, numpy as np

from Exceptions import *

class Rede(ABC):
    def __init__(self):
        self._g = nx.Graph()
        self._wan_adicionada = False
        self._análise_falha_aleatória = None
        self._análise_falha_ataque = None

    def __adicionar_nó(self, nome, tipo):
        self._g.add_node(nome, importância = tipo["importância"], cor = tipo["cor"])

    def _adicionar_wan(self):
        if self._wan_adicionada:
            raise WanException

        self.__adicionar_nó("wan", Constantes.tipos["wan"])
        self._wan_adicionada = True

    def _adicionar_servidores(self, *args):
        for srv in args:
            self.__adicionar_nó("srv:%s" %(srv), Constantes.tipos["servidor"])

    def _adicionar_rtbs(self, *args):
        for rtb in args:
            self.__adicionar_nó("rtb:%s" %(rtb), Constantes.tipos["rtb"])

    def _adicionar_switches_olt(self, *args):
        for switch in args:
            self.__adicionar_nó("swolt:%s" %(switch), Constantes.tipos["switch_olt"])

    def _adicionar_olts(self, *args):
        for olt in args:
            self.__adicionar_nó("olt:%s" %(olt), Constantes.tipos["olt"])

    def _adicionar_roteadores(self, *args):
        for rot in args:
            self.__adicionar_nó("rot:%s" %(rot), Constantes.tipos["roteador"])

    def _adicionar_onus(self, *args):
        for onu in args:
            self.__adicionar_nó("onu:%s" %(onu), Constantes.tipos["onu"])

    def _adicionar_switches_prédio(self, *args):
        for switch in args:
            self.__adicionar_nó("swpr:%s" %(switch), Constantes.tipos["switch_prédio"])

    def _adicionar_paps(self, *args):
        for pap in args:
            self.__adicionar_nó("pap:%s" %(pap), Constantes.tipos["pap"])

    def _adicionar_switches_departamento(self, *args):
        for switch in args:
            self.__adicionar_nó("swdpt:%s" %(switch), Constantes.tipos["switch_departamento"])

    def _adicionar_switches_ramificação(self, *args):
        for switch in args:
            self.__adicionar_nó("swram:%s" %(switch), Constantes.tipos["switch_ramificação"])

    def _adicionar_usuários(self, prefixo, quantidade):
        for i in range(quantidade):
            self.__adicionar_nó("usr:%s_%d" %(prefixo, i+1), Constantes.tipos["usuário"])

    def _adicionar_conexão(self, transmissão_média, transmissão_máxima, latência, início, fim):
        latência_efetiva = latência/(1 - transmissão_média/transmissão_máxima)
        self._g.add_edge(início,fim, transmissão_média = transmissão_média, transmissão_máxima=transmissão_máxima, latência=latência, 
            latência_efetiva = latência_efetiva)

    def desenhar(self):
        plt.figure(figsize=(16,16), dpi=256)

        color_map = []
        for nó in self._g.nodes(data=True):
            color_map.append(nó[1]["cor"])

        nx.draw(self._g, with_labels=True, font_weight='bold', node_color=color_map)
        plt.savefig("./Saída/grafo.png")

    def exportarCSV(self):
        df = pd.DataFrame({"Probabilidade":self._análise_falha_aleatória.probabilidades,
                           "ImportânciasFalha":self._análise_falha_aleatória.importâncias,
                           "LatênciasFalha":self._análise_falha_aleatória.latências,
                           "ImportânciasAtaque": self._análise_falha_ataque.importâncias,
                           "LatênciasAtaque": self._análise_falha_ataque.latências})

        df.to_csv("./Saída/falha_aleatória.csv", sep=";")

    def gerar_gráficos_resiliência(self):
        plt.figure(figsize=(16,16), dpi=256)
        plt.rcParams.update({'font.size': 22})
        plt.suptitle("Análise de Resiliência (Importância e Latência Efetiva)")
        plt.subplots_adjust(hspace=0.3)

        plt.subplot(2,1,1)
        plt.title("Importância x Probabilidade de Remoção")
        plt.plot(self._análise_falha_aleatória.probabilidades, self._análise_falha_aleatória.importâncias, "ro")
        plt.xlabel("Probabilidade de Remoção")
        plt.ylabel("Importância (Normalizada)")
        plt.grid(True, color="Gray")

        plt.subplot(2,1,2)
        plt.title("Latência Efetiva Média x Probabilidade de Remoção")
        plt.plot(self._análise_falha_aleatória.probabilidades, self._análise_falha_aleatória.latências, "bo")
        plt.xlabel("Probabilidade de Remoção")
        plt.ylabel("Latência Efetiva Média (Normalizada)")
        plt.grid(True, color="Gray")

        plt.savefig("./Saída/resiliencia.png")
