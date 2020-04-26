using System;
using Analise.DAO;

namespace Analise.Interfaces
{
    public interface IAnalisador : IDisposable
    {
        AnáliseDAO AnalisarRede(IRede rede);
    }
}