"""
Of Longest Substring

"""


def lengthOfLongestSubstring(s: str) -> int:
    if not s:
        return 0

    char_idx = {}

    l, r = 0, 0
    max_len = 0
    while r < len(s):
        if s[r] in char_idx:
            l = max(l, char_idx[s[r]])
        char_idx[s[r]] = r + 1
        max_len = max(max_len, r - l + 1)
        r += 1
    return max_len


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to lengthOfLongestSubstring
    print(lengthOfLongestSubstring([]))
