namespace Analise.DAO
{
    public class PréCloneDAO
    {
        public string ListaArestas { get; set; }
        public string ListaNós { get; set; }
        
        public PréCloneDAO(string listaArestas, string listaNós)
        {
            ListaArestas = listaArestas;
            ListaNós = listaNós;
        }

    }
}