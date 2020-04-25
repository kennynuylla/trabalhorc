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
                using(IRede clone = rede.Clone() as DebugRede)
                {
                    rede.PlotarRede("/codigo/png/original.png");
                    clone.PlotarRede("/codigo/png/clone.png");
                }
            }
        }
    }
}
