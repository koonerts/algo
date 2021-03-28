using System;
using System.Collections;
using System.Collections.Generic;
using System.Text.Encodings.Web;
using System.Text.Json;

namespace csharp_algo
{
    public static class Extensions
    {
        public static void Println<T>(this T obj)
        {
            Console.WriteLine(JsonSerializer.Serialize(obj, new JsonSerializerOptions{Encoder = JavaScriptEncoder.UnsafeRelaxedJsonEscaping}));
        }

        public static void PrintMatrix(this object matrixObj)
        {
            IEnumerable matrix = (IEnumerable)matrixObj;
            foreach (var row in (IEnumerable) matrixObj)
            {
                row.Println();
            }
        }
    }
}