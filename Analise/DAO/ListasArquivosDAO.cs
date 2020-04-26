namespace Analise.DAO
{
    public class ListasArquivosDAO
    {
        public string ListaArestas { get; set; }
        public string ListaNós { get; set; }
        
        public ListasArquivosDAO(string listaArestas, string listaNós)
        {
            ListaArestas = listaArestas;
            ListaNós = listaNós;
        }

    }
}