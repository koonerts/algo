"""
Find_string_anagrams

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


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to find_string_anagrams
    print(find_string_anagrams([]))
