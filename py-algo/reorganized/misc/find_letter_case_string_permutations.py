"""
Find_letter_case_string_permutations

Given a string, find all of its permutations preserving the character sequence but changing case.

    Example 1:
    Input: "ad52"
    Output: "ad52", "Ad52", "aD52", "AD52"

    Example 2:
    Input: "ab7c"
    Output: "ab7c", "Ab7c", "aB7c", "AB7c", "ab7C", "Ab7C", "aB7C", "AB7C"
"""

from collections import deque


def find_letter_case_string_permutations(str_in: str) -> list[str]:
    """
    Given a string, find all of its permutations preserving the character sequence but changing case.

    Example 1:
    Input: "ad52"
    Output: "ad52", "Ad52", "aD52", "AD52"

    Example 2:
    Input: "ab7c"
    Output: "ab7c", "Ab7c", "aB7c", "AB7c", "ab7C", "Ab7C", "aB7C", "AB7C"
    """
    q = deque([""])
    for c in str_in:
        for _ in range(len(q)):
            current_permutation = q.popleft()
            if c.isalpha():
                q.append(current_permutation + c.lower())
                q.append(current_permutation + c.upper())
            else:
                q.append(current_permutation + c)
    return list(q)


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to find_letter_case_string_permutations
    print(find_letter_case_string_permutations([]))
