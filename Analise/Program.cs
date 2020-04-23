using System;
using PySharp;

namespace Analise
{
    class Program
    {
        static void Main(string[] args)
        {
            var pysharp = new Pysharp("/codigo/py", "python3");
        }
    }
}
