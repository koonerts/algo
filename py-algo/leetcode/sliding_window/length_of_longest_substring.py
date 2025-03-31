"""
Length_of_longest_substring

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


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to length_of_longest_substring
    print(length_of_longest_substring([]))
