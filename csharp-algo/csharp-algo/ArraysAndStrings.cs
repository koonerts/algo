using System.Collections.Generic;

namespace csharp_algo
{
    public class ArraysAndStrings
    {
        public bool IsAlienSorted(string[] words, string order)
        {
            if (words.Length <= 1) return true;

            var alienOrderDict = new Dictionary<char, int>();
            var i = 0;
            foreach (var c in order)
            {
                alienOrderDict[c] = i;
                i++;
            }

            for (i = 1; i < words.Length; i++)
            {
                if (CompareAlienStrings(words[i - 1], words[i], alienOrderDict) == 1)
                    return false;
            }

            return true;
        }

        private int CompareAlienStrings(string str1, string str2, Dictionary<char, int> alienOrderDict)
        {
            int i = 0, j = 0;
            while (i < str1.Length || j < str2.Length)
            {
                if (i >= str1.Length && j < str2.Length) return -1;
                if (i < str1.Length && j >= str2.Length) return 1;
                if (i >= str1.Length && j >= str2.Length) return 0;
                if (alienOrderDict[str1[i]] < alienOrderDict[str2[j]]) return -1;
                if (alienOrderDict[str1[i]] > alienOrderDict[str2[j]]) return 1;
                i++;
                j++;
            }

            return -1;
        }

    }
}