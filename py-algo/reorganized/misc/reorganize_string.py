"""
Reorganize_string

Given a string and a number ‘K’, find if the string can be rearranged such that the same characters are
    at least ‘K’ distance apart from each other.

    Example 1:
    Input: "mmpp", K=2
    Output: "mpmp" or "pmpm"
    Explanation: All same characters are 2 distance apart.

    Example 2:
    Input: "Programming", K=3
    Output: "rgmPrgmiano" or "gmringmrPoa" or "gmrPagimnor" and a few more
    Explanation: All same characters are 3 distance apart.

    Example 3:
    Input: "aab", K=2
    Output: "aba"
    Explanation: All same characters are 2 distance apart.

    Example 4:
    Input: "aappa", K=3
    Output: ""
    Explanation: We cannot find an arrangement of the string where any two 'a' are 3 distance apart.
"""
def reorganize_string(str, k):
    """
    Given a string and a number ‘K’, find if the string can be rearranged such that the same characters are
    at least ‘K’ distance apart from each other.

    Example 1:
    Input: "mmpp", K=2
    Output: "mpmp" or "pmpm"
    Explanation: All same characters are 2 distance apart.

    Example 2:
    Input: "Programming", K=3
    Output: "rgmPrgmiano" or "gmringmrPoa" or "gmrPagimnor" and a few more
    Explanation: All same characters are 3 distance apart.

    Example 3:
    Input: "aab", K=2
    Output: "aba"
    Explanation: All same characters are 2 distance apart.

    Example 4:
    Input: "aappa", K=3
    Output: ""
    Explanation: We cannot find an arrangement of the string where any two 'a' are 3 distance apart.
    """
    # TODO: Come back to
    return ""



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to reorganize_string
    print(reorganize_string([]))
