namespace Analise.DAO
{
    public class MétricasRedeDAO
    {
        public int Importância { get; set; }
        public double Latência { get; set; }
        
        public MétricasRedeDAO(int importância, double latência)
        {
            Importância = importância;
            Latência = latência;
        }
    } 
}