There is a long table with a line of plates and candles arranged on top of it. You are given a 0-indexed string s consisting of characters '*' and '|' only, where a '*' represents a plate and a '|' represents a candle.

You are also given a 0-indexed 2D integer array queries where queries[i] = [lefti, righti] denotes the substring s[lefti...righti] (inclusive). For each query, you need to find the number of plates between candles that are in the substring. A plate is considered between candles if there is at least one candle to its left and at least one candle to its right in the substring.

    For example, s = "||**||**|*", and a query [3, 8] denotes the substring "*||**|". The number of plates between candles in this substring is 2 (at indices 6 and 7), as each of the two plates has at least one candle in the substring to its left and right.

Return an integer array answer where answer[i] is the answer to the ith query.

Example 1:

ex-1

Input: s = "**|**|***|", queries = [[2,5],[5,9]]

Output: [2,3]

Explanation:

    queries[0] has two plates between candles.
    queries[1] has three plates between candles.

Example 2:

ex-2

Input: s = "***|**|*****|**||**|*", queries = [[1,17],[4,5],[14,17],[5,11],[15,16]]

Output: [9,0,0,0,0]

Explanation:

    queries[0] has nine plates between candles.
    The other queries have zero plates between candles.

Constraints:

    3 <= s.length <= 105
    s consists of '*' and '|' characters.
    1 <= queries.length <= 105
    queries[i].length == 2
    0 <= lefti <= righti < s.length

Question

Instead of counting the number of plates between two indices, which takes O(n) time, we can use the indices of the candles to figure out the number of plates between the candles (store in candles).

For each query (qleft, qright), we need to find the two candles on the outside within the boundary [qleft, qright]. This is where binary search comes in.

while left <= right:
   mid = (left+right) // 2
   ### YOUR IMPLEMENTATION HERE ###

Select the correct if-else implementation in the while loop to find:

    the index left_pos in candles of the first candle that is greater than qleft
    the index right_pos in candles of the last candle that is smaller than qright

# 1
if candles[mid] >= qleft:
    right = mid - 1
    left_pos = mid
else:
    left = mid + 1

# 2
if candles[mid] <= qright:
    right = mid - 1
    right_pos = mid
else:
    left = mid + 1

# 1
if candles[mid] >= qleft:
    right = mid - 1
    left_pos = mid
else:
    left = mid + 1

# 2
if candles[mid] <= qright:
    left = mid + 1
    right_pos = mid
else:
    right = mid - 1

# 1
if candles[mid] <= qleft:
    right = mid - 1
    left_pos = mid
else:
    left = mid + 1

# 2
if candles[mid] >= qright:
    left = mid + 1
    right_pos = mid
else:
    right = mid - 1

---

Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

    TimeMap() Initializes the object of the data structure.
    void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
    String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".

Example 1:

Input ["TimeMap", "set", "get", "get", "set", "get", "get"]

[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]

Output

[null, null, "bar", "bar", null, "bar2", "bar2"]

Explanation

TimeMap timeMap = new TimeMap();

timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.

timeMap.get("foo", 1);         // return "bar"

timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".

timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.

timeMap.get("foo", 4);         // return "bar2"

timeMap.get("foo", 5);         // return "bar2"

Constraints:

    1 <= key.length, value.length <= 100
    key and value consist of lowercase English letters and digits.
    1 <= timestamp <= 107
    All the timestamps timestamp of set are strictly increasing.
    At most 2 * 105 calls will be made to set and get.

Question

We want to only store the changes of values for each key chronologically in its own array.

We use a map of string to array histories such that histories[key] is an array that stores pairs (timestamp, value) indicating that key stores value at timestamp.

For the get function, we want to find the value stored in key at timestamp. In histories[key], it is the entry with the greatest timestamp less or equal to the given timestamp.

Given an array history of pairs (timestamp, value) sorted chronologically by timestamp such that the timestamps are distinct, select the correct implementation that finds the correct index pos in history such that history[pos] holds the value of key at timestamp.

left, right, pos = 0, len(history)-1, -1
while left <= right:
    mid = (left+right) // 2
    if history[mid][0] < timestamp:
        left = mid + 1
        pos = mid
    else:
        right = mid - 1

left, right, pos = 0, len(history)-1, -1
while left <= right:
    mid = (left+right) // 2
    if history[mid][1] >= timestamp:
        left = mid + 1
        pos = mid
    else:
        right = mid - 1

left, right, pos = 0, len(history)-1, -1
while left <= right:
    mid = (left+right) // 2
    if history[mid][0] <= timestamp:
        pos = mid
        right = mid - 1
    else:
        left = mid + 1

left, right, pos = 0, len(history)-1, -1
while left <= right:
    mid = (left+right) // 2
    if history[mid][0] <= timestamp:
        left = mid + 1
        pos = mid
    else:
        right = mid - 1

---

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:

Input: s = "hello"
Output: "holle"

Example 2:

Input: s = "leetcode"
Output: "leotcede"

Constraints:

    1 <= s.length <= 3 * 105
    s consist of printable ASCII characters.

Question

Select the correct pseudocode implementation to reverse vowels. Define string.swap(i,j) to swap the characters at position i and j of string.

l, r = 0, len(s)-1
while l < r:
    if s[l] in vowels:
        l += 1
    elif s[r] in vowels:
        r -= 1
    else:
        s.swap(l, r)
        l += 1
        r -= 1

l, r = 0, len(s)-1
while l < r:
    if s[l] not in vowels:
        l += 1
    elif s[r] not in vowels:
        r -= 1
    else:
        s.swap(l, r)

l, r = 0, len(s)-1
while l < r:
    if s[l] not in vowels:
        l += 1
    elif s[r] not in vowels:
        r -= 1
    else:
        s.swap(l, r)
        l += 1
        r -= 1

l, r = 0, len(s)-1
while l < r:
    if s[l] not in vowels:
        l += 1
    if s[r] not in vowels:
        r -= 1
    else:
        s.swap(l, r)
        l += 1
        r -= 1


---


Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:

Input: s = "aba"
Output: true

Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

Example 3:

Input: s = "abc"
Output: false

Constraints:

    1 <= s.length <= 105
    s consists of lowercase English letters.

Question

Given an isPalindrome(string) helper function that returns true when string is a palindrome. Select the best (correct and efficient) implementation for validPalindrome(s) true when s is a palindrome (after at most one character is removed).

def validPalindrome(self, s: str) -> bool:
    l, r = 0, len(s)-1
    while l < r:
        if s[l] != s[r]:
            return isPalindrome(s[l+1:r+1]) or isPalindrome(s[l:r])
        l += 1
        r -= 1
    return True

def validPalindrome(self, s: str) -> bool:
    for i in range(len(s)):
        string = s[0:i] + s[i+1:]
        if isPalindrome(string):
            return True
    return False

def validPalindrome(self, s: str) -> bool:
    reverse = s[::-1]   # reverses s
    removed = 0
    for c in range(len(s)):
        if reverse[c] != s[c]:
            removed += 1
    if removed <= 1:
        return True
    else:
        return False