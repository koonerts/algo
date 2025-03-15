"""
Of Longest Substring Two Distinct

"""

import collections


def lengthOfLongestSubstringTwoDistinct(s: str) -> int:
    if len(s) <= 2:
        return len(s)

    char_freq = collections.defaultdict(lambda: 0)
    l, max_substr_len = 0, 0
    for r, c in enumerate(s):
        char_freq[c] += 1
        while len(char_freq) > 2:
            if char_freq[s[l]] == 1:
                del char_freq[s[l]]
            else:
                char_freq[s[l]] -= 1
            l += 1
        max_substr_len = max(max_substr_len, r - l + 1)
    return max_substr_len


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to lengthOfLongestSubstringTwoDistinct
    print(lengthOfLongestSubstringTwoDistinct([]))
