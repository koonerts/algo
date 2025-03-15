"""
Non_repeat_substring

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

        max_ = max(max_, i-start+1)

    return max_



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to non_repeat_substring
    print(non_repeat_substring([]))
