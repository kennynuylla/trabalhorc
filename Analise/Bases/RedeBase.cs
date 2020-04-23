using System;
using System.IO;
using Analise.Interfaces;
using PySharp;

namespace Analise.Bases
{
    public abstract class RedeBase : IRede
    {
        private const string _pastaTodasRedes = "Redes/";
        private const string _arquivoCriar = "criar.py";
        private const string _diretórioTmp = "tmp/";
        private const string _baseNomeListaArestas = "rede_arestas";
        private const string _extensão = ".txt";

        private readonly string _caminhoPython;
        private readonly string _listaArestas;

        public string DiretórioTmp { get => $"{_caminhoPython}{_pastaTodasRedes}{_caminhoRede}{_diretórioTmp}";}
        public string ListaArestas { get => $"{DiretórioTmp}{_listaArestas}"; }
        public string ScriptCriarRelativo { get => $"{_pastaTodasRedes}{_caminhoRede}{_arquivoCriar}"; }

        protected readonly Pysharp _pysharp;
        protected readonly string _caminhoRede;

        public RedeBase(string caminhoPython, string caminhoRede, string executávelPython)
        {
            _pysharp = new Pysharp(caminhoPython, executávelPython);
            _caminhoRede = caminhoRede;
            _caminhoPython = caminhoPython;

            var tmpListaArestas = _baseNomeListaArestas;
            var aleatório = new Random();

            if(!Directory.Exists(DiretórioTmp))
            {
                Directory.CreateDirectory(DiretórioTmp);
            }
            
            while(File.Exists($"{DiretórioTmp}{tmpListaArestas}{_extensão}"))
            {
                tmpListaArestas = $"{tmpListaArestas}{aleatório.Next(10)}";
            }

            _listaArestas = $"{tmpListaArestas}{_extensão}";
            File.Create(ListaArestas);
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
    }
}