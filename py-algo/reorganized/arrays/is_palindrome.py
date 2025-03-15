"""
Palindrome

"""


def isPalindrome(s: str) -> bool:
    if s == "":
        return True

    start, end = 0, len(s) - 1
    while start <= end:
        while (not s[start].isalnum()) and start < end:
            start += 1
        while (not s[end].isalnum()) and start < end:
            end -= 1

        if s[start].casefold() != s[end].casefold():
            return False

        start += 1
        end -= 1
    return True


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to isPalindrome
    print(isPalindrome([]))
