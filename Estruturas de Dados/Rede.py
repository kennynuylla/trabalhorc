from abc import ABC, abstractmethod
import networkx as nx, matplotlib.pyplot as plt, Constantes

import WanAdicionadaException as WanException

class Rede(ABC):
    def __init__(self):
        self._g = nx.Graph()
        self._wan_adicionada = False

    def adicionar_wan(self):
        if wan_adicionada:
            raise WanException()

        self._g.add_node("wan", importância = Constantes.tipos["wan"]["importância"], cor = Constantes.tipos["wan"]["cor"])

    def desenhar(self):
        plt.figure(figsize=(16,16), dpi=256)

        color_map = []
        for nó in self.g.nodes(data=True):
            color_map.append(nó[1]["cor"])

        nx.draw(self._g, with_labels=True, font_weight='bold', node_color=color_map)
        plt.savefig("./Saída/grafo.png")