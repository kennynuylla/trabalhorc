namespace Analise.DAO
{
    public class ListaArquivosDAO
    {
        public string ListaArestas { get; set; }
        public string ListaNós { get; set; }
        
        public ListaArquivosDAO(string listaArestas, string listaNós)
        {
            ListaArestas = listaArestas;
            ListaNós = listaNós;
        }

    }
}