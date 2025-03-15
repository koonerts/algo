"""
Find_permutation

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


import string
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



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to find_permutation
    print(find_permutation([]))
