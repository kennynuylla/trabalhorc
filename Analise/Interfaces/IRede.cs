using System;
using Analise.DAO;

namespace Analise.Interfaces
{
    public interface IRede : IDisposable, ICloneable
    {
        void CriarRede();
        void PlotarRede(string arquivo);
        ListasArquivosDAO RetornarArquivosRede();
    }
}