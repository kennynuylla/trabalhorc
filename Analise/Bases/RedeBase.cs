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

        private int _importânciaTotal;
        private double _latênciaEfetivaMédia;
        private string _listaNós;
        private string _listaArestas;

        protected readonly Pysharp _pysharp;
        protected readonly string _caminhoRede;

        public string DiretórioTmp { get => $"{_caminhoPython}{_constantes.PastaTodasRedes}{_caminhoRede}{_constantes.DiretórioTmp}";}
        public string ListaArestas { get => $"{DiretórioTmp}{_listaArestas}"; }
        public string ListaNós { get => $"{DiretórioTmp}{_listaNós}"; }

        public string ScriptCriarRelativo { get => $"{_constantes.PastaTodasRedes}{_caminhoRede}{_constantes.ArquivoCriar}"; }
        public string ScriptPlotarRelativo { get => $"{_constantes.PastaTodasRedes}{_caminhoRede}{_constantes.ArquivoPlotar}"; }


        public RedeBase(string caminhoPython, string caminhoRede, string executávelPython)
        {
            _pysharp = new Pysharp(caminhoPython, executávelPython);
            _caminhoRede = caminhoRede;
            _caminhoPython = caminhoPython;

            CriarDiretórioTemporário();
            CriarArquivoListaArestas();
            CriarArquivoListaNós();
        }

        public virtual void CriarRede()
        {
            _pysharp.LimparArgumentos();

            _pysharp.AdicionarArgumento(ListaArestas);
            _pysharp.AdicionarArgumento(ListaNós);

            var resposta = _pysharp.Executar(ScriptCriarRelativo);
            var dadosRede = resposta.MensagensTela.Split('|', 2, StringSplitOptions.RemoveEmptyEntries);
            _importânciaTotal = Int32.Parse(dadosRede[0]);
            _latênciaEfetivaMédia = Double.Parse(dadosRede[1]);
        
        }

        public void PlotarRede(string arquivo)
        {
            _pysharp.LimparArgumentos();

            _pysharp.AdicionarArgumento(ListaNós);
            _pysharp.AdicionarArgumento(ListaArestas);
            _pysharp.AdicionarArgumento(arquivo);

            var resposta = _pysharp.Executar(ScriptPlotarRelativo);
        }

        public void Dispose()
        {
            File.Delete(ListaArestas);
            File.Delete(ListaNós);
        }

        private void CriarDiretórioTemporário()
        {
            if (!Directory.Exists(DiretórioTmp))
            {
                Directory.CreateDirectory(DiretórioTmp);
            }
        }

        private void CriarArquivoListaArestas()
        {
            _listaArestas = $"{ObterNomeArquivo(_constantes.BaseNomeListaArestas)}{_constantes.Extensão}";
            File.Create(ListaArestas);

        }

        private string ObterNomeArquivo(string baseNome)
        {
            var aleatório = new Random();
            while(File.Exists($"{DiretórioTmp}{baseNome}{_constantes.Extensão}"))
            {
                baseNome = $"{baseNome}{aleatório.Next(10)}";
            }

            return baseNome;
        }

        private void CriarArquivoListaNós()
        {
            _listaNós = $"{ObterNomeArquivo(_constantes.BaseNomeListaNós)}{_constantes.Extensão}";
            File.Create(ListaNós);
        }
    }
}