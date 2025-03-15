"""
Array By Parity

Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.
        You may return any answer array that satisfies this condition.

        Input: [3,1,2,4]
        Output: [2,4,3,1]
        The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
"""


def sortArrayByParity(a: list[int]) -> list[int]:
    """
    Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.
    You may return any answer array that satisfies this condition.

    Input: [3,1,2,4]
    Output: [2,4,3,1]
    The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
    """
    i = 0
    p_even = 0
    while i < len(a):
        if a[i] % 2 == 1:
            for j in range(p_even, len(a)):
                if a[j] % 2 == 0 and j > i:
                    v = a[j]
                    a[j] = a[i]
                    a[i] = v
                    p_even = j + 1
                    break
                p_even += 1
        i += 1

    return a


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to sortArrayByParity
    print(sortArrayByParity([]))
