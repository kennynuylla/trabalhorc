using System;

namespace Analise.Interfaces
{
    public interface IRede : IDisposable
    {
        void CriarRede();
        void PlotarRede(string arquivo);
    }
}