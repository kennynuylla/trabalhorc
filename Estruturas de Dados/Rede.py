from abc import ABC, abstractmethod
import networkx as nx, matplotlib.pyplot as plt, Constantes

class Rede(ABC):
    def __init__(self):
        self.g = nx.Graph()
        self.g.add_node(Constantes.switches["geral"], tipo=Constantes.tipos["switch"], cor=Constantes.cores["cinza"])
        self.g.add_node(Constantes.roteadores["cidade_digital"], tipo=Constantes.tipos["roteador"], cor=Constantes.cores["vermelho"])
        self.g.add_node(Constantes.pontos["internet"], tipo=Constantes.tipos["internet"], cor=Constantes.cores["amarelo"])
        self.g.add_node(Constantes.switches["anexo_2"], tipo=Constantes.tipos["switch"], cor=Constantes.cores["cinza"])
        self.g.add_node(Constantes.switches["sec_educação"], tipo=Constantes.tipos["switch"], cor=Constantes.cores["cinza"])
        self.g.add_node(Constantes.switches["sec_saúde"], tipo=Constantes.tipos["switch"], cor=Constantes.cores["cinza"])

        self.g.add_edge(Constantes.pontos["internet"], Constantes.roteadores["cidade_digital"])
        self.g.add_edge(Constantes.roteadores["cidade_digital"], Constantes.switches["geral"])
        self.adicionar_switch_roteador(Constantes.switches["anexo_2"])
        self.adicionar_switch_roteador(Constantes.switches["sec_educação"])
        self.adicionar_switch_roteador(Constantes.switches["sec_saúde"])

    def inserir_rh(self):
        self.adicionar_switch(Constantes.switches["RH"], Constantes.switches["geral"])
        self.conectar_switch(Constantes.switches["RH"], Constantes.usuários["RH"], "RH")

    def inserir_administração(self):
        self.conectar_switch(Constantes.switches["geral"], Constantes.usuários["ADM"], "ADM", "roxo")

    def inserir_comunicação(self):
        self.conectar_switch(Constantes.switches["geral"], Constantes.usuários["COM"], "COM", "azul")

    def inserir_ti(self):
        self.conectar_switch(Constantes.switches["geral"], Constantes.usuários["TI"], "TI", "verde")

    def inserir_projetos(self):
        self.conectar_switch(Constantes.switches["geral"], Constantes.usuários["PROJ"], "PROJ", "laranja")

    def inserir_gab_vice_prefeito(self):
        self.conectar_switch(Constantes.switches["geral"], Constantes.usuários["VICE"], "VICE", "ciano")

    def inserir_gab_prefeito(self):
        self.conectar_switch(Constantes.switches["geral"], Constantes.usuários["PREF"], "PREF", "amarelo")

    def inserir_recepção_protocolo(self):
        self.conectar_switch(Constantes.switches["geral"], Constantes.usuários["RP"], "RP", "magenta")

    def inserir_cpl(self):
        self.adicionar_switch(Constantes.switches["CPL"], Constantes.switches["geral"])
        self.conectar_switch(Constantes.switches["CPL"], Constantes.usuários["CPL"], "CPL")

    def inserir_controladoria(self):
        self.conectar_switch(Constantes.switches["geral"], Constantes.usuários["CTR"], "CTR", "marrom")

    def inserir_governo(self):
        self.conectar_switch(Constantes.switches["geral"], Constantes.usuários["GOV"], "GOV", "lima")

    def inserir_procuradoria(self):
        self.conectar_switch(Constantes.switches["geral"], Constantes.usuários["PROC"], "PROC", "ouro")

    def inserir_fazenda(self):
        self.conectar_switch(Constantes.switches["geral"], Constantes.usuários["FAZ"], "FAZ", "rosa"),

    def inserir_contabilidade(self):
        self.adicionar_switch(Constantes.switches["CONT"], Constantes.switches["geral"])
        self.conectar_switch(Constantes.switches["CONT"], Constantes.usuários["CONT"], "CONT")
    
    def inserir_porto_rapido(self):
        self.adicionar_switch_roteador(Constantes.switches["porto_rápido"])
        self.conectar_switch(Constantes.switches["porto_rápido"], Constantes.usuários["PORTO"], "PORTO")

    def inserir_saúde(self):
        self.adicionar_switch(Constantes.switches["saúde_geral_01"], Constantes.switches["sec_saúde"])
        self.adicionar_switch(Constantes.switches["saúde_geral_02"], Constantes.switches["sec_saúde"])

        self.conectar_switch(Constantes.switches["saúde_geral_01"], Constantes.usuários["SAÚDE01"], "S1")
        self.conectar_switch(Constantes.switches["saúde_geral_02"], Constantes.usuários["SAÚDE02"], "S2")

    def inserir_educação(self):
        self.conectar_switch(Constantes.switches["sec_educação"], Constantes.usuários["EDUCAÇÃO"], "EDU")

    def conectar_switch(self, nome_switch, número_conexões, prefixo, cor = "azul"):
        for i in range(número_conexões):
            nome = "%s_%d" %(prefixo, i+1)
            self.g.add_node(nome, cor=Constantes.cores[cor], tipo=Constantes.tipos["usuário"])
            self.g.add_edge(nome_switch, nome)
            

    def montar(self):
        self.inserir_rh()
        self.inserir_administração()
        self.inserir_comunicação()
        self.inserir_ti()
        self.inserir_projetos()
        self.inserir_gab_vice_prefeito()
        self.inserir_recepção_protocolo()
        self.inserir_cpl()
        self.inserir_controladoria()
        self.inserir_gab_prefeito()
        self.inserir_governo()
        self.inserir_procuradoria()
        self.inserir_fazenda()
        self.inserir_contabilidade()
        self.inserir_porto_rapido()
        self.inserir_saúde()
        self.inserir_educação()

    def adicionar_switch(self, início, fim):
        self.g.add_node(início, tipo=Constantes.tipos["switch"], cor=Constantes.cores["cinza"])
        self.g.add_edge(início, fim)

    def adicionar_switch_roteador(self, nome):
        self.g.add_node(nome, tipo=Constantes.tipos["switch"], cor=Constantes.cores["cinza"])
        self.g.add_edge(nome, Constantes.roteadores["cidade_digital"]) 

    def desenhar(self):
        plt.figure(figsize=(16,16), dpi=256)

        color_map = []
        for nó in self.g.nodes(data=True):
            color_map.append(nó[1]["cor"])

        nx.draw(self.g, with_labels=True, font_weight='bold', node_color=color_map)
        plt.savefig("./Saída/grafo.png")