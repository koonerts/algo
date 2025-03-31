"""
Window

"""


def minWindow(s: str, t: str) -> str:
    left, right = 0, 0
    char_freq = {}

    ret_str = ""
    while right < len(s):
        if s[right] in t:
            char_freq[s[right]] = char_freq.get(s[right], 0) + 1


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to minWindow
    print(minWindow([]))
