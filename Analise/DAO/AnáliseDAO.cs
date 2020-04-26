namespace Analise.DAO
{
    public class AnáliseDAO
    {

        public double[] ImportânciaTotal { get; set; }
        public double[] LatênciaEfetivaMédia { get; set; }
        public double[] TaxaRemoção { get; set; }
        
        public AnáliseDAO(double[] importânciaTotal, double[] latênciaEfetivaMédia, double[] taxaRemoção)
        {
            ImportânciaTotal = importânciaTotal;
            LatênciaEfetivaMédia = latênciaEfetivaMédia;
            TaxaRemoção = taxaRemoção;
        }
    }
}