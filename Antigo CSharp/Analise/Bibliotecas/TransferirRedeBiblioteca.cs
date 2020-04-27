using System;
using System.Collections;
using System.Collections.Generic;
using System.IO;

namespace Analise.Bibliotecas
{
    public class TransferirRedeBiblioteca : IEnumerable<string>, IEnumerator<string>, IDisposable
    {
        private readonly FileStream _streamLeitura;
        private readonly StreamReader _arquivoLeitura;
        private readonly FileStream _streamEscrita;
        private readonly StreamWriter _arquivoEscrita;
        private readonly string _arquivoOriginal;
        private string _linha;
        
        public string ArquivoBackup { get => $"{_arquivoOriginal}.bkp"; }

        public string Current => _linha;
        object IEnumerator.Current => throw new NotImplementedException();

        public TransferirRedeBiblioteca(string arquivoOriginal)
        {
            _arquivoOriginal = arquivoOriginal;
            File.Move(_arquivoOriginal, ArquivoBackup);

            _streamLeitura = File.Open(ArquivoBackup, FileMode.Open);
            _arquivoLeitura = new StreamReader(_streamLeitura);

            _streamEscrita = File.Open(_arquivoOriginal, FileMode.CreateNew);
            _arquivoEscrita = new StreamWriter(_streamEscrita);
        }

        public void Dispose()
        {
            _arquivoLeitura.Dispose();
            _arquivoEscrita.Dispose();
            _streamLeitura.Dispose();
            _streamEscrita.Dispose();
            File.Delete(ArquivoBackup);
        }

        public bool MoveNext()
        {
            _linha = _arquivoLeitura.ReadLine();
            return _linha != null;
        }

        public IEnumerator<string> GetEnumerator()
        {
            return this;
        }


        public void Escrever()
        {
            _arquivoEscrita.WriteLine(Current);
        }


        public void Reset()
        {
            throw new NotImplementedException();
        }


        IEnumerator IEnumerable.GetEnumerator()
        {
            throw new NotImplementedException();
        }
    }
}