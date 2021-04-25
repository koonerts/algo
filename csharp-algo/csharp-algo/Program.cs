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

    public sealed class Singleton
    {
        private static readonly Lazy<Singleton> lazy = new(() => new Singleton());
        private Singleton() { }
        public static Singleton Instance => lazy.Value;
    }

    public class FizzBuzz
    {
        private int _n;
        private static int count = 1;
        private object _baton = new();

        public FizzBuzz(int n)
        {
            _n = n;
        }

        private void SyncRun(Func<int, bool> condition, Action<int> action)
        {
            while (true)
            {
                lock (_baton)
                {

                    if (count > _n)
                        return;

                    if (condition(count))
                    {
                        action(count);
                        count++;
                    }
                }
            }
        }

        // printFizz() outputs "fizz".
        public void Fizz(Action printFizz)
        {
            SyncRun(i => i % 3 == 0 && i % 5 != 0, x => printFizz());
        }

        // printBuzzz() outputs "buzz".
        public void Buzz(Action printBuzz)
        {
            SyncRun(i => i % 5 == 0 && i % 3 != 0, x => printBuzz());
        }

        // printFizzBuzz() outputs "fizzbuzz".
        public void Fizzbuzz(Action printFizzBuzz)
        {
            SyncRun(i => i % 3 == 0 && i % 5 == 0, x => printFizzBuzz());
        }

        // printNumber(x) outputs "x", where x is an integer.
        public void Number(Action<int> printNumber)
        {
            SyncRun(i => i % 3 != 0 && i % 5 != 0, x => printNumber(x));
        }
    }
}