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


def longest_substring_with_k_distinct(str: str, k: int) -> int:
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
    for i, c in enumerate(str):
        if c not in distinct_map:
            distinct_map[c] = 1
        else:
            distinct_map[c] += 1

        while len(distinct_map) > k:
            if distinct_map[str[start]] - 1 == 0:
                distinct_map.pop(str[start])
            else:
                distinct_map[str[start]] -= 1

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

        max_ = max(max_, i-start+1)

    return max_


def non_repeat_substring(str: str) -> int:
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

    for i, c in enumerate(str):
        char_map[c] = (char_map.get(c) or 0) + 1

        while char_map[c] > 1:
            if char_map[str[start]] == 1:
                del char_map[str[start]]
            else:
                char_map[str[start]] -= 1

            start += 1

        max_ = max(max_, i-start+1)

    return max_


def length_of_longest_substring(str: str, k: int):
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

    start, next, max_ = 0, 0, 0
    start_char = str[start]
    char_map = {}

    for i, c in enumerate(str):
        if c != start_char:
            char_map[c] = (char_map.get(c) or 0) + 1


print(non_repeat_substring('abccde'))