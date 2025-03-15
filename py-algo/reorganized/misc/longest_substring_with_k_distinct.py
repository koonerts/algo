"""
Longest_substring_with_k_distinct

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


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to longest_substring_with_k_distinct
    print(longest_substring_with_k_distinct([]))
