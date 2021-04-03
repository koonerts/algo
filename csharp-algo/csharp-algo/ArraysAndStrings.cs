using System;
using System.Collections.Generic;
using System.Linq;

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

        public int MaxNumberOfBalloons(string text)
        {
            var balFreq = new int[26];
            foreach (var c in text)
            {
                balFreq[c - 'a']++;
            }
            var minSingles = 1<<31-1;
            var minDoubles = 1<<31-1;
            var singles = new[] { 'b' - 'a', 'a' - 'a', 'n' - 'a' };
            var doubles = new[] { 'l' - 'a', 'o' - 'a' };
            for (var i = 0; i < balFreq.Length; i++)
            {
                if (singles.Contains(i))
                {
                    minSingles = Math.Min(minSingles, balFreq[i]);
                }
                else if (doubles.Contains(i))
                {
                    minDoubles = Math.Min(minDoubles, balFreq[i]);
                }
            }

            if (minSingles == 0 || minDoubles < 2)
                return 0;
            if (minDoubles <= minSingles * 2)
                return minDoubles / 2;
            return minSingles;
        }

        public int MinCost(string s, int[] cost)
        {
            var idxStk = new Stack<int>();
            idxStk.Push(0);
            var minCost = 0;
            for (var i = 1; i < s.Length; i++)
            {
                if (s[i] != s[idxStk.Peek()])
                {
                    idxStk.Pop();
                    idxStk.Push(i);
                }
                else
                {
                    if (cost[idxStk.Peek()] < cost[i])
                    {
                        minCost += cost[idxStk.Pop()];
                        idxStk.Push(i);
                    }
                    else
                    {
                        minCost += cost[i];
                    }
                }
            }

            return minCost;
        }

        public int MaxLengthUniqueConcat(IList<string> arr)
        {
            var charSets = new List<HashSet<char>>(arr.Count);
            foreach (var str in arr)
            {
                charSets.Add(new HashSet<char>());
                foreach (var c in str)
                {
                    charSets[^1].Add(c);
                }
            }

            var maxLen = 0;
            void dfs(int idx, HashSet<char> currSet)
            {
                maxLen = Math.Max(maxLen, currSet.Count);
                if (idx >= arr.Count)
                    return;
                if (!currSet.Overlaps(charSets[idx]))
                    dfs(idx + 1, currSet.Union(charSets[idx]).ToHashSet());
                dfs(idx + 1, currSet);
            }

            dfs(0, new HashSet<char>());
            return maxLen;
        }

        public int TestGroupScores(string[] T, string[] R) {
            int testGroupIdx = 0;
            while (testGroupIdx < T[0].Length && T[0][testGroupIdx].IsLowerAlpha())
                testGroupIdx++;

            var statusMap = new Dictionary<string, bool>();
            for (var i = 0; i < T.Length; i++)
            {
                string test = T[i];
                int numIdxEnd = testGroupIdx;
                while (numIdxEnd < test.Length && test[numIdxEnd].IsNumeric())
                    numIdxEnd++;

                string testGroup = test.Substring(0, numIdxEnd);
                if (statusMap.ContainsKey(testGroup) && !statusMap[testGroup])
                    continue;

                statusMap[testGroup] = R[i] == "OK";
            }

            int passedCount = 0;
            foreach (var kvp in statusMap)
            {
                if (kvp.Value == true)
                    passedCount++;
            }
            return (passedCount*100)/statusMap.Count;
        }

    }
}