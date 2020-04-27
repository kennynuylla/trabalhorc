using System;
using Analise.DAO;
using Analise.Interfaces;

namespace Analise.Bibliotecas
{
    public class AnalisadorEmMemória : IAnalisador
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
               var dados = rede.AnalisarEmMemória(probabilidade);
               importânciaTotal[i] = dados.Importância;
               latênciaEfetiva[i] = dados.Latência;
               Console.WriteLine($"Analisado {i+1} de {_quantidadePontos}");
           }

           return new AnáliseDAO(importânciaTotal, latênciaEfetiva, probabilidadesRemoção, _quantidadePontos);
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
    }
}