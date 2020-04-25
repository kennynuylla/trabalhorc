using System;

namespace Analise.Interfaces
{
    public interface IRede : IDisposable, ICloneable
    {
        void CriarRede();
        void PlotarRede(string arquivo);
    }
}