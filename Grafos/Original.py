import Rede, Constantes

class Original(Rede.Rede):
    def montar(self):
        self._adicionar_wan()
        self._adicionar_servidores("nat", "dns", "arquivos", "vmware1", "vmware2", "ad")
        self._adicionar_rtbs("rtb")
        self._adicionar_switches_olt("sw_l2")
        self._adicionar_olts("peas", "pag1", "pag2")
        self._adicionar_roteadores("prefeitura")

        #Onus
        peas = ["pcg0.%d" %(i) for i in range(1,21)]
        self._adicionar_onus(*peas)

        for onu in peas:
            self._adicionar_conexão(200, 1000, 16, "onu:%s" %(onu), "olt:peas")



