using System;
using Analise.DAO;

namespace Analise.Interfaces
{
    public interface IRede : IDisposable, ICloneable
    {
        void CriarRede();
        void PlotarRede(string arquivo);
        void Reanalisar();
        ListaArquivosDAO RetornarArquivosRede();
        MétricasRedeDAO RetornarMétricasRede();
        MétricasRedeDAO AnalisarEmMemória(double probabilidadeRemoção);
    }
}