from abc import ABC, abstractmethod
import networkx as nx, matplotlib.pyplot as plt, Constantes

from Exceptions import *

class Rede(ABC):
    def __init__(self):
        self._g = nx.Graph()
        self._wan_adicionada = False

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
        self._g.add_edge(início,fim, transmissão_média = transmissão_média, transmissão_máxima=transmissão_máxima, latência=latência)

    def desenhar(self):
        plt.figure(figsize=(16,16), dpi=256)

        color_map = []
        for nó in self._g.nodes(data=True):
            color_map.append(nó[1]["cor"])

        nx.draw(self._g, with_labels=True, font_weight='bold', node_color=color_map)
        plt.savefig("./Saída/grafo.png")