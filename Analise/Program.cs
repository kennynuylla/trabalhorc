using System;
using Analise.Interfaces;
using Analise.Redes;

namespace Analise
{
    class Program
    {
        static void Main(string[] args)
        {
            using(IRede rede = new DebugRede())
            {
                rede.CriarRede();
            }
        }
    }
}
