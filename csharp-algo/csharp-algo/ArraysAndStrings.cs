using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

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
            if (arr.Count == 0) return 0;
            if (arr.Count == 1) return arr[0].Length;

            var charSets = new List<HashSet<char>>(arr.Count);
            foreach (var str in arr)
            {
                var charSet = new HashSet<char>();
                foreach (var ch in str)
                {
                    if (charSet.Contains(ch))
                    {
                        charSet.Clear();
                        break;
                    }

                    charSet.Add(ch);
                }
                charSets.Add(charSet);
            }

            int maxLen = 0;
            void dfs(int idx, HashSet<char> currCharSet)
            {
                maxLen = Math.Max(maxLen, currCharSet.Count);
                if (idx >= charSets.Count)
                    return;

                if (!currCharSet.Overlaps(charSets[idx]))
                    dfs(idx + 1, currCharSet.Union(charSets[idx]).ToHashSet());
                dfs(idx + 1, currCharSet);
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

        public int[] SumZero(int n)
        {
            var result = new List<int>(n);
            var sum = 0;
            for (var i = 1; i <= n; i++)
            {
                result.Add(i);
                sum += i;
            }

            result[^1] = -(sum - result[^1]);
            return result.ToArray();
        }

        public int FirstMissingPositive(int[] nums)
        {
            bool oneExists = false;
            for (var i = 0; i < nums.Length; i++)
            {
                if (!oneExists && nums[i] == 1)
                    oneExists = true;
                if (nums[i] <= 0 || nums[i] > nums.Length)
                {
                    nums[i] = 1;
                }
            }

            if (!oneExists)
                return 1;

            for (var i = 0; i < nums.Length; i++)
            {
                if (nums[Math.Abs(nums[i]) - 1] > 0)
                    nums[Math.Abs(nums[i]) - 1] = -nums[Math.Abs(nums[i]) - 1];
            }

            for (var i = 0; i < nums.Length; i++)
            {
                if (nums[i] > 0)
                    return i + 1;
            }
            return nums.Length+1;
        }

        public int MinPathSum(int[][] grid)
        {
            for (var i = 0; i < grid.Length; i++)
            {
                for (var j = 0; j < grid[i].Length; j++)
                {
                    if (i == 0 && j > 0)
                        grid[i][j] += grid[i][j - 1];
                    else if (i > 0 && j == 0)
                        grid[i][j] += grid[i - 1][j];
                    else if (i > 0 && j > 0)
                        grid[i][j] += Math.Min(grid[i][j - 1], grid[i - 1][j]);
                }
            }

            return grid[^1][^1];
        }

        public String CountAndSay(int n) {
            if(n==1) return "1";
            string ans = "1";
            for(int i=2; i<=n; i++){
                ans = f(ans);
            }
            return ans;
        }

        private string f(string s){
            char ch = s[0];
            int count = 1;
            StringBuilder sb = new();
            for (var i = 1; i < s.Length; i++){
                if (s[i] != ch) {
                    sb.Append(count).Append(ch);
                    ch = s[i];
                    count = 1;
                } else {
                    count++;
                }
            }
            sb.Append(count).Append(ch);
            return sb.ToString();
        }
    }
}