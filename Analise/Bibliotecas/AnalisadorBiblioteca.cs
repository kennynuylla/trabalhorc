using System;
using System.Collections.Generic;
using System.IO;
using System.Text.RegularExpressions;
using Analise.DAO;
using Analise.Interfaces;

namespace Analise.Bibliotecas
{
    public class AnalisadorBiblioteca : IAnalisador
    {
        private const int _quantidadePontos = 100;

        public AnáliseDAO AnalisarRede(IRede rede)
        {
           var probabilidadesRemoção = Linspace(0,1,_quantidadePontos);
           var importânciaTotal = new double[_quantidadePontos];
           var latênciaEfetiva = new double[_quantidadePontos];

           for (int i = 0; i < _quantidadePontos; i++)
           {
               var probabilidade = probabilidadesRemoção[i];
               using(IRede clone = rede.Clone() as IRede)
               {
                   RemoverNós(clone, probabilidade);
                   clone.Reanalisar();
               }
               Console.WriteLine($"Analisado {i+1} de {_quantidadePontos}");
           }

           return new AnáliseDAO(importânciaTotal, latênciaEfetiva, probabilidadesRemoção);
        }

        public void Dispose()
        {
            throw new System.NotImplementedException();
        }

        private double [] Linspace (double início, double fim, int quantidade)
        {
            double[] retorno = new double[quantidade];
            double incremento = (fim - início)/quantidade;
            double valor = início;

            for(int i = 0; i < quantidade - 1; i++)
            {
                retorno[i] = valor;
                valor += incremento;
            }
            retorno[quantidade - 1] = fim;

            return retorno;
        }

        private void RemoverNós(IRede rede, double probabilidadeRemoção)
        {
            var aleatório = new Random();
            var nósRemovidos = new List<string>();
            var arquivos = rede.RetornarArquivosRede();

            using(var transferência = new TransferirRedeBiblioteca(arquivos.ListaNós))
            {
                foreach (var item in transferência)
                {
                    var valor = aleatório.NextDouble();
                    if(valor <= probabilidadeRemoção) 
                    {
                        var nó = item.Split(" ", 3, StringSplitOptions.RemoveEmptyEntries)[0];
                        nósRemovidos.Add(nó);
                        continue;
                    }

                    transferência.Escrever();
                }
            }

            using (var transferência = new TransferirRedeBiblioteca(arquivos.ListaArestas))
            {
                foreach (var item in transferência)
                {
                    var deletar = false;
                    foreach (var nó in nósRemovidos)
                    {
                        var regex1 = new Regex($"^[{nó}][ ][0-9]");
                        var regex2 = new Regex($"^[0-9][ ][{nó}]");

                        var teste1 = regex1.IsMatch(item);
                        var teste2 = regex2.IsMatch(item);

                        if(teste1 || teste2)
                        {
                            deletar = true;
                            break;
                        }
                    }

                    if(deletar) continue;

                    transferência.Escrever();
                }
            }
        }
    }
}