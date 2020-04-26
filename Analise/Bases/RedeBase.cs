using System;
using System.IO;
using Analise.Constantes;
using Analise.DAO;
using Analise.Interfaces;
using PySharp;
using PySharp.DAO;

namespace Analise.Bases
{
    public abstract class RedeBase : IRede
    {
        protected readonly RedeBaseConstantes _constantes = new RedeBaseConstantes();
        private string _caminhoPython;
        private string _executávelPython;
        private string _caminhoRede;

        protected int _importânciaTotal;
        protected double _latênciaEfetivaMédia;
        protected string _listaNós;
        protected string _listaArestas;
        protected Pysharp _pysharp;

        public string DiretórioTmp { get => $"{_caminhoPython}{_constantes.PastaTodasRedes}{_caminhoRede}{_constantes.PastaTemporária}";}
        public string ListaArestas { get => $"{DiretórioTmp}{_listaArestas}"; }
        public string ListaNós { get => $"{DiretórioTmp}{_listaNós}"; }
        public string ScriptCriarRelativo { get => $"{_constantes.PastaTodasRedes}{_caminhoRede}{_constantes.ArquivoCriar}"; }
        public string ScriptPlotarRelativo { get => $"{_constantes.PastaScriptsComuns}{_constantes.ArquivoPlotar}"; }
        public string ScriptReanalisarRelativo { get => $"{_constantes.PastaScriptsComuns}{_constantes.ArquivoReanalisar}"; }

        public RedeBase(string caminhoPython, string caminhoRede, string executávelPython)
        {
            InicializarPython(caminhoPython, caminhoRede, executávelPython);
            CriarDiretório(DiretórioTmp);
            CriarArquivoListaArestas();
            CriarArquivoListaNós();
        }

        public RedeBase(string caminhoPython, string caminhoRede, string executávelPython, string listaArestas, string listaNós,
            int importânciaTotal, double latênciaEfetiva)
        {
            InicializarPython(caminhoPython, caminhoRede, executávelPython);    
            _listaArestas = listaArestas;
            _listaNós = listaNós;
            _importânciaTotal = importânciaTotal;
            _latênciaEfetivaMédia = latênciaEfetiva;
        }

        public virtual void CriarRede()
        {
            InserirArgumentosPadrão();

            var resposta = _pysharp.Executar(ScriptCriarRelativo);
            ExtrairAnálise(resposta);

        }

        public void PlotarRede(string arquivo)
        {
            CriarDiretório(_constantes.PastaPlots);
            InserirArgumentosPadrão();

            _pysharp.AdicionarArgumento(arquivo);

            var resposta = _pysharp.Executar(ScriptPlotarRelativo);
        }

        public void Dispose()
        {
            File.Delete(ListaArestas);
            File.Delete(ListaNós);
        }

        public ListaArquivosDAO RetornarArquivosRede()
        {
            return new ListaArquivosDAO(ListaArestas, ListaNós);
        }

        public abstract object Clone();

        public void Reanalisar()
        {
            InserirArgumentosPadrão();

            var resposta = _pysharp.Executar(ScriptReanalisarRelativo);
            ExtrairAnálise(resposta);
        }

        public MétricasRedeDAO RetornarMétricasRede() => new MétricasRedeDAO(_importânciaTotal, _latênciaEfetivaMédia);

        private void CriarDiretório(string diretório)
        {
            if (!Directory.Exists(diretório))
            {
                Directory.CreateDirectory(diretório);
            }
        }

        private void CriarArquivoListaArestas()
        {
            _listaArestas = $"{ObterNomeArquivo(_constantes.BaseNomeListaArestas)}{_constantes.Extensão}";
            CriarArquivo(ListaArestas);

        }

        private void CriarArquivoListaNós()
        {
            _listaNós = $"{ObterNomeArquivo(_constantes.BaseNomeListaNós)}{_constantes.Extensão}";
            CriarArquivo(ListaNós);
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

        private void InicializarPython(string caminhoPython, string caminhoRede, string executávelPython)
        {
            _pysharp = new Pysharp(caminhoPython, executávelPython);
            _caminhoRede = caminhoRede;
            _caminhoPython = caminhoPython;
            _executávelPython = executávelPython;
        }

        private void CriarArquivo(string arquivo)
        {
            File.Create(arquivo).Close(); //A função Create abre o arquivo criado
        }

        private void ExtrairAnálise(ProcessoDAO resposta)
        {
            var dadosRede = resposta.MensagensTela.Split('|', 2, StringSplitOptions.RemoveEmptyEntries);
            _importânciaTotal = Int32.Parse(dadosRede[0]);
            _latênciaEfetivaMédia = Double.Parse(dadosRede[1]);
        }

        private void InserirArgumentosPadrão()
        {
            _pysharp.LimparArgumentos();
            _pysharp.AdicionarArgumento(ListaNós);
            _pysharp.AdicionarArgumento(ListaArestas);
        }

        protected ListaArquivosDAO PréClone()
        {
            var listaArestasClone = $"{ObterNomeArquivo(_constantes.BaseNomeListaArestas)}{_constantes.Extensão}";
            var listaNósClone = $"{ObterNomeArquivo(_constantes.BaseNomeListaNós)}{_constantes.Extensão}";

            File.Copy(ListaArestas, $"{DiretórioTmp}{listaArestasClone}");
            File.Copy(ListaNós, $"{DiretórioTmp}{listaNósClone}");

            return new ListaArquivosDAO(listaArestasClone, listaNósClone);
        }
    }
}