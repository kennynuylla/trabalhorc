using System;
using System.Globalization;
using System.IO;
using Analise.DAO;

namespace Analise.Bibliotecas
{
    public class CSVResultado : IDisposable
    {
        private const string _diretórioBase = "/codigo/";
        private const string _diretórioCsv = "csv/";

        private readonly string _arquivo;
        private readonly char _separador;
        private readonly FileStream _streamEscrita;
        private readonly StreamWriter _arquivoEscrita;
        private readonly AnáliseDAO _análise;

        public string DiretórioCSV { get => $"{_diretórioBase}{_diretórioCsv}"; }
        public string ArquivoCSV { get => $"{DiretórioCSV}{_arquivo}"; }

        public CSVResultado(string arquivo, char separador, AnáliseDAO análise)
        {
            _arquivo = arquivo;
            _separador = separador;
            
            if(!Directory.Exists(DiretórioCSV))
            {
                Directory.CreateDirectory(DiretórioCSV);
            }

            File.Create(ArquivoCSV).Close();

            _streamEscrita = File.Open(ArquivoCSV, FileMode.Create);
            _arquivoEscrita = new StreamWriter(_streamEscrita);
            _análise = análise;

        }

        public void Escrever()
        {
            _arquivoEscrita.WriteLine($"TaxaRemoção{_separador}ImportânciaTotal{_separador}LatênciaEfetivaMédia");
            for (int i = 0; i < _análise.QuantidadePontos; i++)
            {
                var taxa = _análise.TaxaRemoção[i];
                var importância = _análise.ImportânciaTotal[i];
                var latência = _análise.LatênciaEfetivaMédia[i];

                _arquivoEscrita.WriteLine($"{taxa}{_separador}{importância}{_separador}{latência}");
            }
        }

        public void Dispose()
        {
            _arquivoEscrita.Dispose();
            _streamEscrita.Dispose();
        }
    }
}