using Analise.Bases;
using PySharp;

namespace Analise.Redes
{
    public class DebugRede : RedeBase
    {

        private readonly static string _caminhoPython = "/codigo/py/";
        private readonly static string _caminhoRede = "Debug/";
        private readonly static string _executávelPython = "python3";

        public DebugRede() : base(_caminhoPython, _caminhoRede, _executávelPython)
        {

        }

        public DebugRede(string listaArestas, string listaNós, int importância, double latência) :
            base(_caminhoPython, _caminhoRede, _executávelPython, listaArestas, listaNós, importância, latência)
            {

            }

        public override object Clone()
        {
            var dados = base.PréClone();

            var clone = new DebugRede(dados.ListaArestas, dados.ListaNós, _importânciaTotal, _latênciaEfetivaMédia);
            return clone;
        }
    }
}