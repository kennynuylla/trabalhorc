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
                Console.WriteLine("Rede Criada");

                IAnalisador analisador = new AnalisadorBiblioteca();
                analisador.AnalisarRede(rede);
                Console.WriteLine("Rede Analisada");
            }
        }
    }
}
