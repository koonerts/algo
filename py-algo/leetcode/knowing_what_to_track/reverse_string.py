"""
String

Write a function that reverses a string. The input string is given as an array of characters char[].
        Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
"""


def reverseString(s: list[str]) -> None:
    """
    Write a function that reverses a string. The input string is given as an array of characters char[].
    Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
    """
    l, r = 0, len(s) - 1
    while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to reverseString
    print(reverseString([]))
