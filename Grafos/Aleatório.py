import Rede, Constantes, networkx as nx, numpy as np, AnáliseResultadosDAO, Analisador


class Aleatório(Rede.Rede):

    def __init__(self):
        self.__tipos = list(Constantes.tipos.keys())
        self.__tipos.remove("wan")

        total_importâncias = sum(Constantes.tipos[x]["importância"] for x in self.__tipos)
        self.__probabilidade_tipos = [Constantes.tipos[x]["importância"]/total_importâncias for x in self.__tipos] #142 é o somatório das importância sem wan

    def _adicionar_tipo(self, nó, wan = False):
        if wan:
            nó["importância"] = Constantes.tipos["wan"]["importância"]
            nó["cor"] = Constantes.tipos["wan"]["cor"]
        else:
            chave = np.random.choice(self.__tipos, p = self.__probabilidade_tipos)
            nó["importância"] = Constantes.tipos[chave]["importância"]
            nó["cor"] = Constantes.tipos[chave]["cor"]

    def montar(self):
        self._g = nx.fast_gnp_random_graph(2000, 0.3)
        nós = self._g.nodes(data=True)
        self._adicionar_tipo(nós[0], True)

        for i in range(1, len(nós)):
            self._adicionar_tipo(nós[i])

        latência_máxima = 1 #conexão entre duas placas geralment é menor que 1ms
        transmissão_máxima = 1000 #Mbps

        for aresta in self._g.edges(data=True):
            latência = np.random.rand() * latência_máxima
            transmissão = np.random.rand() * transmissão_máxima

            aresta[2]["latência"] = latência
            aresta[2]["transmissão_média"] = transmissão
            aresta[2]["transmissão_máxima"] = transmissão_máxima

    def analisar(self):
        self._análise_falha_aleatória = AnáliseResultadosDAO.AnáliseResultadosDAO(*Analisador.gerar_pontos_resiliência(self._g, 100,100))