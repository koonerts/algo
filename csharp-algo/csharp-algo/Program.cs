using System;

namespace csharp_algo
{
    class Program
    {
        static void Main(string[] args)
        {
            var words = new string[3] { "word", "world", "row" };
            new ArraysAndStrings().IsAlienSorted(words, "worldabcefghijkmnpqstuvxyz");
        }
    }
}