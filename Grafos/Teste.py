import Rede, Analisador, AnáliseResultadosDAO

class Teste(Rede.Rede):

    def montar(self):
        self._adicionar_wan()
        self._adicionar_roteadores("principal")
        self._adicionar_servidores("ad", "arquivos")
        self._adicionar_switches_departamento("srvs", "adm")
        self._adicionar_usuários("adm", 3)

        #conexões

        #ADM
        adm = ["usr:adm_%d" %(i+1) for i in range(3)]
        latências = [16,1,10]
        taxas = [150, 120, 110]

        for i in range(3):
            self._adicionar_conexão(taxas[i], 200, latências[i], adm[i], "swdpt:adm")


        #SRVs
        self._adicionar_conexão(110,200,5, "srv:ad", "swdpt:srvs")
        self._adicionar_conexão(123,200,1, "srv:arquivos", "swdpt:srvs")

        #Switches
        self._adicionar_conexão(197, 200, 3, "swdpt:srvs", "rot:principal")
        self._adicionar_conexão(130, 200, 10, "swdpt:adm", "rot:principal")

        #Roteador
        self._adicionar_conexão(230, 1000, 11, "rot:principal", "wan")

    def analisar(self):
        self._análise_falha_aleatória = AnáliseResultadosDAO.AnáliseResultadosDAO(*Analisador.gerar_pontos_resiliência(self._g, 100,100))