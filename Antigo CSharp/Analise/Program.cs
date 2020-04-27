using System;
using System.IO;
using Analise.Bibliotecas;
using Analise.Interfaces;
using Analise.Redes;

namespace Analise
{
    class Program
    {
        static void Main(string[] args)
        {
            // TestarPlotEImportância();
            // TestarClone();
            TestarAnálise();
        }

        public static void TestarPlotEImportância()
        {
            var png = "/codigo/png/original.png";
            using(IRede rede = new DebugRede())
            {
                rede.CriarRede();
                rede.PlotarRede(png);
            } //Verificar se plot está certo e se a importância total também
            File.Delete(png);
        }

        public static void TestarClone()
        {
            var pngOriginal = "/codigo/png/original.png";
            var pngClone = "/codigo/png/clone.png";
            using(IRede rede = new DebugRede())
            {
                rede.CriarRede();
                using(IRede clone = rede.Clone() as DebugRede)
                {
                    rede.PlotarRede(pngOriginal);
                    clone.PlotarRede(pngClone);
                }
            }

            File.Delete(pngClone);
            File.Delete(pngOriginal);
        }

        public static void TestarAnálise()
        {
            using(IRede rede = new DebugRede())
            {
                rede.CriarRede();
                Console.WriteLine("Rede Criada");
                IAnalisador analisador = new AnalisadorEmMemória();
                var dados = analisador.AnalisarRede(rede);

                using(var resultado = new CSVResultado("analise.csv", ';', dados))
                {
                    resultado.Escrever();
                }
            }
        }
    }
}
