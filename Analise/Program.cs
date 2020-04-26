using System;
using Analise.Bibliotecas;
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
/*                IRede clone = rede.Clone() as DebugRede;
                rede.PlotarRede("/codigo/png/original.png");
                clone.PlotarRede("/codigo/png/clone.png");
                Console.WriteLine("Rede Criada");
*/
                IAnalisador analisador = new AnalisadorBiblioteca();
                analisador.AnalisarRede(rede);
                Console.WriteLine("Rede Analisada");
            }
        }
    }
}
