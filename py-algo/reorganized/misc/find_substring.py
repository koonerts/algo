"""
Find_substring

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


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to find_substring
    print(find_substring([]))
