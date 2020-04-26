using System;
using Analise.DAO;

namespace Analise.Interfaces
{
    public interface IAnalisador
    {
        AnáliseDAO AnalisarRede(IRede rede);
    }
}