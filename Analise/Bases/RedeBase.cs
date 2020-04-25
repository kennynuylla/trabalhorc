using System;
using System.IO;
using Analise.Constantes;
using Analise.DAO;
using Analise.Interfaces;
using PySharp;

namespace Analise.Bases
{
    public abstract class RedeBase : IRede
    {
        protected readonly RedeBaseConstantes _constantes = new RedeBaseConstantes();
        private readonly string _caminhoPython;
        private readonly string _executávelPython;
        private readonly string _caminhoRede;

        protected int _importânciaTotal;
        protected double _latênciaEfetivaMédia;
        protected string _listaNós;
        protected string _listaArestas;

        protected readonly Pysharp _pysharp;

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
            _executávelPython = executávelPython;

            CriarDiretórioTemporário();
            CriarArquivoListaArestas();
            CriarArquivoListaNós();
        }

        public RedeBase(string caminhoPython, string caminhoRede, string executávelPython, string listaArestas, string listaNós,
            int importânciaTotal, double latênciaEfetiva)
        {
            _pysharp = new Pysharp(caminhoPython, executávelPython);
            _caminhoPython = caminhoPython;
            _caminhoRede = caminhoRede;
            _executávelPython = executávelPython;
            _listaArestas = listaArestas;
            _listaNós = listaNós;
            _importânciaTotal = importânciaTotal;
            _latênciaEfetivaMédia = latênciaEfetiva;
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

            if(!Directory.Exists(_constantes.PastaPlots))
            {
                Directory.CreateDirectory(_constantes.PastaPlots);
            }

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

        public abstract object Clone();

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
            File.Create(ListaArestas).Close(); //A função Create abre o arquivo criado;

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
            File.Create(ListaNós).Close();
        }

        protected PréCloneDAO PréClone()
        {
            var listaArestasClone = $"{ObterNomeArquivo(_constantes.BaseNomeListaArestas)}{_constantes.Extensão}";
            var listaNósClone = $"{ObterNomeArquivo(_constantes.BaseNomeListaNós)}{_constantes.Extensão}";

            File.Copy(ListaArestas, $"{DiretórioTmp}{listaArestasClone}");
            File.Copy(ListaNós, $"{DiretórioTmp}{listaNósClone}");

            return new PréCloneDAO(listaArestasClone, listaNósClone);
        }

    }
}