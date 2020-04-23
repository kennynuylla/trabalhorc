using System;
using System.IO;
using Analise.Constantes;
using Analise.Interfaces;
using PySharp;

namespace Analise.Bases
{
    public abstract class RedeBase : IRede
    {
        private readonly RedeBaseConstantes _constantes = new RedeBaseConstantes();
        private readonly string _caminhoPython;
        private readonly string _listaArestas;

        protected readonly Pysharp _pysharp;
        protected readonly string _caminhoRede;

        public string DiretórioTmp { get => $"{_caminhoPython}{_constantes.PastaTodasRedes}{_caminhoRede}{_constantes.DiretórioTmp}";}
        public string ListaArestas { get => $"{DiretórioTmp}{_listaArestas}"; }
        public string ScriptCriarRelativo { get => $"{_constantes.PastaTodasRedes}{_caminhoRede}{_constantes.ArquivoCriar}"; }


        public RedeBase(string caminhoPython, string caminhoRede, string executávelPython)
        {
            _pysharp = new Pysharp(caminhoPython, executávelPython);
            _caminhoRede = caminhoRede;
            _caminhoPython = caminhoPython;

            CriarDiretórioTemporário();
            _listaArestas = CriarArquivoListaArestas();
            
        }


        public virtual void CriarRede()
        {
            _pysharp.AdicionarArgumento(ListaArestas);
            var resposta = _pysharp.Executar(ScriptCriarRelativo);

            if(resposta.AlgoErrado) 
            {
                //Lançar Exceção
            }
        }

        public void Dispose()
        {
            File.Delete(ListaArestas);
        }

        private void CriarDiretórioTemporário()
        {
            if (!Directory.Exists(DiretórioTmp))
            {
                Directory.CreateDirectory(DiretórioTmp);
            }
        }

        private string CriarArquivoListaArestas()
        {
            string retorno;

            var tmpListaArestas = _constantes.BaseNomeListaArestas;
            var aleatório = new Random();

            while (File.Exists($"{DiretórioTmp}{tmpListaArestas}{_constantes.Extensão}"))
            {
                tmpListaArestas = $"{tmpListaArestas}{aleatório.Next(10)}";
            }

            retorno = $"{tmpListaArestas}{_constantes.Extensão}";
            File.Create(retorno);

            return retorno;
        }
    }
}