using System;
using System.Collections.Generic;
using System.Text.Json;
using csharp_algo.Collections;

namespace csharp_algo
{
    class Program
    {
        static void Main(string[] args)
        {
            var result = new ArraysAndStrings().TestGroupScores(
                new[] { "codility1", "codility3", "codility50", "codility4b", "codility4a" },
                new[] { "Wrong answer", "OK", "OK", "Runtime error", "OK" }
                );

            Println(result);
        }

        static void Println(object? val)
        {
            Console.WriteLine(val);
        }
    }
}