def max_sub_array_of_size_k(k: int, arr: list[int]) -> int:
    """
    Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.

    Example 1:
    Input: [2, 1, 5, 1, 3, 2], k=3
    Output: 9
    Explanation: Subarray with maximum sum is [5, 1, 3].

    Example 2:
    Input: [2, 3, 4, 1, 5], k=2
    Output: 7
    Explanation: Subarray with maximum sum is [3, 4].
    """
    start, max_sum, curr_sum = 0, 0, 0
    for i in range(len(arr)):
        if i - start + 1 <= k:
            curr_sum += arr[i]
        else:
            curr_sum -= arr[start]
            start += 1
            curr_sum += arr[i]

        if curr_sum > max_sum:
            max_sum = curr_sum

    return max_sum


def smallest_subarray_with_given_sum(s: int, arr: list[int]) -> int:
    """
    Given an array of positive numbers and a positive number ‘S,’ find the length of the smallest contiguous subarray
    whose sum is greater than or equal to ‘S’. Return 0 if no such subarray exists.

    Example 1:
    Input: [2, 1, 5, 2, 3, 2], S=7
    Output: 2
    Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].

    Example 2:
    Input: [2, 1, 5, 2, 8], S=7
    Output: 1
    Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].

    Example 3:
    Input: [3, 4, 1, 1, 6], S=8
    Output: 3
    Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] or [1, 1, 6].
    """
    start, curr_sum, min_length = 0, 0, len(arr) + 1
    for window_end in range(0, len(arr)):
        curr_sum += arr[window_end]  # add the next element

        # shrink the window as small as possible until the 'curr_sum' is smaller than 's'
        while curr_sum >= s:
            min_length = min(min_length, window_end - start + 1)
            curr_sum -= arr[start]
            start += 1
    if min_length > len(arr):
        return 0
    return min_length


def longest_substring_with_k_distinct(str_: str, k: int) -> int:
    """
    Given a string, find the length of the longest substring in it with no more than K distinct characters.

    Example 1:
    Input: String="araaci", K=2
    Output: 4
    Explanation: The longest substring with no more than '2' distinct characters is "araa".

    Example 2:
    Input: String="araaci", K=1
    Output: 2
    Explanation: The longest substring with no more than '1' distinct characters is "aa".

    Example 3:
    Input: String="cbbebi", K=3
    Output: 5
    Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".
    """
    distinct_map = {}
    start = 0
    max_len = 0
    for i, c in enumerate(str_):
        if c not in distinct_map:
            distinct_map[c] = 1
        else:
            distinct_map[c] += 1

        while len(distinct_map) > k:
            if distinct_map[str_[start]] - 1 == 0:
                distinct_map.pop(str_[start])
            else:
                distinct_map[str_[start]] -= 1

            start += 1

        curr_len = i - start + 1
        if curr_len > max_len:
            max_len = curr_len

    return max_len


def fruits_into_baskets(fruits: list[str]) -> int:
    """
    Given an array of characters where each character represents a fruit tree, you are given two baskets, and your goal is
    to put maximum number of fruits in each basket. The only restriction is that each basket can have only one type of fruit.

    You can start with any tree, but you can’t skip a tree once you have started.
    You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.
    Write a function to return the maximum number of fruits in both the baskets.

    Example 1:
    Input: Fruit=['A', 'B', 'C', 'A', 'C']
    Output: 3
    Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']

    Example 2:
    Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
    Output: 5
    Explanation: We can put 3 'B' in one basket and two 'C' in the other basket.
                 This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']
    """
    fruit_map = {}
    start, max_ = 0, 0

    for i, f in enumerate(fruits):
        if not fruit_map.get(f):
            fruit_map[f] = 1
        else:
            fruit_map[f] += 1

        while len(fruit_map) > 2:
            if fruit_map[fruits[start]] == 1:
                del fruit_map[fruits[start]]
            else:
                fruit_map[fruits[start]] -= 1

            start += 1

        max_ = max(max_, i - start + 1)

    return max_


def non_repeat_substring(str_: str) -> int:
    """
    Given a string, find the length of the longest substring, which has no repeating characters.

    Example 1:
    Input: String="aabccbb"
    Output: 3
    Explanation: The longest substring without any repeating characters is "abc".

    Example 2:
    Input: String="abbbb"
    Output: 2
    Explanation: The longest substring without any repeating characters is "ab".

    Example 3:
    Input: String="abccde"
    Output: 3
    Explanation: Longest substrings without any repeating characters are "abc" & "cde".
    """
    char_map = {}
    start, max_ = 0, 0

    for i, c in enumerate(str_):
        char_map[c] = char_map.get(c, 0) + 1

        while char_map[c] > 1:
            if char_map[str_[start]] == 1:
                del char_map[str_[start]]
            else:
                char_map[str_[start]] -= 1

            start += 1

        max_ = max(max_, i - start + 1)

    return max_


def length_of_longest_substring(str_: str, k: int) -> int:
    """
    Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter,
    find the length of the longest substring having the same letters after replacement.

    Example 1:
    Input: String="aabccbb", k=2
    Output: 5
    Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".

    Example 2:
    Input: String="abbcb", k=1
    Output: 4
    Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".

    Example 3:
    Input: String="abccde", k=1
    Output: 3
    Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".
    """

    start, max_substring_len, max_repeat_cntr = 0, 0, 0
    char_map = {}

    for i, c in enumerate(str_):
        char_map[c] = char_map.get(c, 0) + 1
        max_repeat_cntr = max(max_repeat_cntr, char_map[c])

        window_len = i - start + 1
        if window_len - max_repeat_cntr > k:
            if char_map[str_[start]] == 1:
                del char_map[str_[start]]
            else:
                char_map[str_[start]] -= 1

            start += 1
            window_len -= 1

        max_substring_len = max(max_substring_len, window_len)
    return max_substring_len


def length_of_longest_subarray(arr: list[int], k: int) -> int:
    """
    Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, find the length of the longest contiguous subarray having all 1s.

    Example 1:
    Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
    Output: 6
    Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.

    Example 2:
    Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3
    Output: 9
    Explanation: Replace the '0' at index 6, 9, and 10 to have the longest contiguous subarray of 1s having length 9.
    """
    start, max_subarray_len, max_repeat_cntr = 0, 0, 0
    bit_map = {}

    for i, v in enumerate(arr):
        bit_map[v] = bit_map.get(v, 0) + 1
        max_repeat_cntr = max(max_repeat_cntr, bit_map[v])
        window_len = i - start + 1

        if window_len - max_repeat_cntr > k:
            if bit_map[arr[start]] == 1:
                del bit_map[arr[start]]
            else:
                bit_map[arr[start]] -= 1

            start += 1
            window_len -= 1

        max_subarray_len = max(max_subarray_len, window_len)
    return max_subarray_len


def find_permutation(str_: str, pattern: str):
    """
    Given a string and a pattern, find out if the string contains any permutation of the pattern.
    Permutation is defined as the re-arranging of the characters of the string. For example, “abc” has the following six permutations:

    abc, acb, bac, bca, cab, cba
    If a string has ‘n’ distinct characters, it will have n! permutations.

    Example 1:
    Input: String="oidbcaf", Pattern="abc"
    Output: true
    Explanation: The string contains "bca" which is a permutation of the given pattern.

    Example 2:
    Input: String="odicf", Pattern="dc"
    Output: false
    Explanation: No permutation of the pattern is present in the given string as a substring.

    Example 3:
    Input: String="bcdxabcdy", Pattern="bcdyabcdx"
    Output: true
    Explanation: Both the string and the pattern are a permutation of each other.

    Example 4:
    Input: String="aaacb", Pattern="abc"
    Output: true
    Explanation: The string contains "acb" which is a permutation of the given pattern.
    """
    start, pattern_map = 0, {}

    for c in pattern:
        pattern_map[c] = pattern_map.get(c, 0) + 1

    for i, c in enumerate(str_):
        if c in pattern_map:
            pattern_map[c] -= 1
            while pattern_map[c] < 0:
                if str_[start] in pattern_map:
                    pattern_map[str_[start]] += 1
                start += 1
        else:
            while start <= i:
                if str_[start] in pattern_map:
                    pattern_map[str_[start]] += 1
                start += 1

        if i - start + 1 == len(pattern):
            return True
    return False


def find_string_anagrams(str_: str, pattern: str) -> list[int]:
    """
    Given a string and a pattern, find all anagrams of the pattern in the given string.
    Anagram is actually a Permutation of a string. For example, “abc” has the following six anagrams:
    abc, acb, bac, bca, cab, cba

    Write a function to return a list of starting indices of the anagrams of the pattern in the given string.

    Example 1:
    Input: String="ppqp", Pattern="pq"
    Output: [1, 2]
    Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".

    Example 2:
    Input: String="abbcabc", Pattern="abc"
    Output: [2, 3, 4]
    Explanation: The three anagrams of the pattern in the given string are "bca", "cab", and "abc".
    """

    result_indexes = []
    start, pattern_map = 0, {}

    for c in pattern:
        pattern_map[c] = pattern_map.get(c, 0) + 1

    for i, c in enumerate(str_):
        if c not in pattern_map:
            while start <= i:
                if str_[start] in pattern_map:
                    pattern_map[str_[start]] += 1
                start += 1
        else:
            while pattern_map[c] <= 0:
                pattern_map[str_[start]] += 1
                start += 1
            pattern_map[c] -= 1

        if i - start + 1 == len(pattern):
            result_indexes.append(start)
            pattern_map[str_[start]] += 1
            start += 1

    return result_indexes


def find_substring(str_: str, pattern: str) -> str:
    """
    Given a string and a pattern, find the smallest substring in the given string which has all the characters of the given pattern.

    Example 1:
    Input: String="aabdec", Pattern="abc"
    Output: "abdec"
    Explanation: The smallest substring having all characters of the pattern is "abdec"

    Example 2:
    Input: String="abdbca", Pattern="abc"
    Output: "bca"
    Explanation: The smallest substring having all characters of the pattern is "bca".

    Example 3:
    Input: String="adcad", Pattern="abc"
    Output: ""
    Explanation: No substring in the given string has all characters of the pattern.
    """
    start, solved, pattern_map = 0, 0, {}
    min_substr = ""

    for c in pattern:
        pattern_map[c] = pattern_map.get(c, 0) + 1

    for i, c in enumerate(str_):
        if c in pattern_map:
            pattern_map[c] -= 1

            if pattern_map[c] == 0:
                solved += 1
            elif pattern_map[c] < 0:
                while str_[start] not in pattern_map or pattern_map[str_[start]] < 0:
                    if str_[start] in pattern_map:
                        pattern_map[str_[start]] += 1
                    start += 1

        if solved == len(pattern_map):
            if min_substr == "" or i - start + 1 < len(min_substr):
                min_substr = str_[start : i + 1]

    return min_substr


# TODO: Come back to: https://www.educative.io/courses/grokking-the-coding-interview/Y5YDWzqPn7O
def find_word_concatenation(str, words):
    """
    Given a string and a list of words, find all the starting indices of substrings in the given string that are a
    concatenation of all the given words exactly once without any overlapping of words.
    It is given that all words are of the same length.

    Example 1:
    Input: String="catfoxcat", Words=["cat", "fox"]
    Output: [0, 3]
    Explanation: The two substring containing both the words are "catfox" & "foxcat".

    Example 2:
    Input: String="catcatfoxfox", Words=["cat", "fox"]
    Output: [3]
    Explanation: The only substring containing both the words is "catfox".
    """
    result_indices = []
    return result_indices


print(find_word_concatenation("abdbca", "abc"))
