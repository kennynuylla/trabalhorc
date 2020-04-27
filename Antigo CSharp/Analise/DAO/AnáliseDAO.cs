namespace Analise.DAO
{
    public class AnáliseDAO
    {

        public double[] ImportânciaTotal { get; }
        public double[] LatênciaEfetivaMédia { get; }
        public double[] TaxaRemoção { get; }
        public int QuantidadePontos { get; }
        
        public AnáliseDAO(double[] importânciaTotal, double[] latênciaEfetivaMédia, double[] taxaRemoção, int quantidadePontos)
        {
            ImportânciaTotal = importânciaTotal;
            LatênciaEfetivaMédia = latênciaEfetivaMédia;
            TaxaRemoção = taxaRemoção;
            QuantidadePontos = quantidadePontos;
        }
    }
}