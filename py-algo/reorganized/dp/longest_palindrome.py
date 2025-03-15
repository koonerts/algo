"""
Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.

Example:
    Input: babad
    Output: bab (Note: aba is also a valid answer)
    
Time Complexity: O(n²) where n is the length of the string
Space Complexity: O(1) as we only need constant extra space
"""

def longestPalindrome(s: str) -> str:
    """
Given a string s, return the longest palindromic substring in s.

Args:
    s (str): Input string
    
Returns:
    str: Longest palindromic substring
    
Time Complexity: O(n²) where n is the length of the string
Space Complexity: O(1) as we only need constant extra space
"""
    pass



    # Example usage
    if __name__ == "__main__":
    # TODO: Add example calls to longestPalindrome
    print(longestPalindrome([]))




# Example usage
if __name__ == "__main__":
    longestPalindrome("babad")  # Output: "bab" or "aba"
    longestPalindrome("cbbd")  # Output: "bb"
    longestPalindrome("a")  # Output: "a"
