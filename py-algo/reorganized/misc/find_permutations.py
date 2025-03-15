"""
Find_permutations

Given a set of distinct numbers, find all of its permutations.
    Permutation is defined as the re-arranging of the elements of the set.
    For example, {1, 2, 3} has the following six permutations:

    {1, 2, 3}
    {1, 3, 2}
    {2, 1, 3}
    {2, 3, 1}
    {3, 1, 2}
    {3, 2, 1}

    If a set has ‘n’ distinct elements it will have n! permutations.

    Example 1:
    Input: [1,3,5]
    Output: [1,3,5], [1,5,3], [3,1,5], [3,5,1], [5,1,3], [5,3,1]
"""


from collections import deque
def find_permutations(nums: list[int]):
    """
    Given a set of distinct numbers, find all of its permutations.
    Permutation is defined as the re-arranging of the elements of the set.
    For example, {1, 2, 3} has the following six permutations:

    {1, 2, 3}
    {1, 3, 2}
    {2, 1, 3}
    {2, 3, 1}
    {3, 1, 2}
    {3, 2, 1}

    If a set has ‘n’ distinct elements it will have n! permutations.

    Example 1:
    Input: [1,3,5]
    Output: [1,3,5], [1,5,3], [3,1,5], [3,5,1], [5,1,3], [5,3,1]
    """
    if not nums: return []
    result = []
    q: deque[list[int]] = deque()

    for i, num in enumerate(nums):
        if i == 0:
            q.append([num])
            continue

        q_len = len(q)
        for _ in range(q_len):
            set_ = q.popleft()
            for j in range(len(set_) + 1):
                set_copy = list(set_)
                set_copy.insert(j, num)

                if len(set_copy) == len(nums):
                    result.append(set_copy)
                else:
                    q.append(set_copy)

    return result



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to find_permutations
    print(find_permutations([]))
