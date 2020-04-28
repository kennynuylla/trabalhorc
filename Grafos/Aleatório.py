import Rede, Constantes, networkx as nx, numpy as np, AnáliseResultadosDAO, Analisador


class Aleatório(Rede.Rede):

    def __init__(self):
        self.__tipos = list(Constantes.tipos.keys())
        self.__tipos.remove("wan")

        total_importâncias = sum(Constantes.tipos[x]["importância"] for x in self.__tipos)
        self.__probabilidade_tipos = [Constantes.tipos[x]["importância"]/total_importâncias for x in self.__tipos] #142 é o somatório das importância sem wan

    def _adicionar_tipo(self, nó, wan = False):
        if wan:
            importância = Constantes.tipos["wan"]["importância"]
            nó["importância"] = importância
            nó["cor"] = Constantes.tipos["wan"]["cor"]

        else:
            chave = np.random.choice(self.__tipos, p = self.__probabilidade_tipos)
            importância = Constantes.tipos[chave]["importância"]

            nó["importância"] = importância
            nó["cor"] = Constantes.tipos[chave]["cor"]


    def montar(self, quantidade_nós, taxa_conexão):
        self._g = nx.fast_gnp_random_graph(quantidade_nós, taxa_conexão)
        print("Debug: qtd_nós = %d e taxa = %f" %(quantidade_nós, taxa_conexão))
        nós = self._g.nodes(data=True)
        self._adicionar_tipo(nós[0], True)

        for i in range(1, len(nós)):
            self._adicionar_tipo(nós[i])

        latência_máxima = 1 #conexão entre duas placas geralment é menor que 1ms
        transmissão_máxima = 1000 #Mbps

        for aresta in self._g.edges(data=True):
            latência = np.random.rand() * latência_máxima
            transmissão = np.random.rand() * transmissão_máxima
            latência_efetiva = latência/(1 - transmissão/transmissão_máxima)

            aresta[2]["latência"] = latência
            aresta[2]["latência_efetiva"] = latência_efetiva

        self.latência_efetiva_média = nx.average_shortest_path_length(self._g, weight="latência_efetiva")

    def analisar(self, quantidade_repetições, quantidade_probabilidades):
        self._análise_falha_aleatória = AnáliseResultadosDAO.AnáliseResultadosDAO(*Analisador.gerar_pontos_falha(self._g, quantidade_repetições,
            quantidade_probabilidades))

        self._análise_falha_ataque = AnáliseResultadosDAO.AnáliseResultadosDAO(*Analisador.gerar_pontos_ataque(self._g, quantidade_repetições,
            quantidade_probabilidades))