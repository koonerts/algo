using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.Json;
using csharp_algo.Collections;

namespace csharp_algo
{
    class Program
    {
        static void Main(string[] args)
        {
            Println(new ArraysAndStrings().CountAndSay(4));
        }

        static void Println(object? val)
        {
            Console.WriteLine(val);
        }
    }

    /*public sealed class Singleton
    {
        private static readonly Lazy<Singleton> lazy = new(() => new Singleton());
        private Singleton() { }
        public static Singleton Instance => lazy.Value;
    }*/
}