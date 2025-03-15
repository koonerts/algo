"""
Max Consecutive Ones

Given a binary array, find the maximum number of consecutive 1s in this array if you can flip at most one 0.

        Input: [1,0,1,1,0]
        Output: 4
        Explanation: Flip the first zero will get the the maximum number of consecutive 1s.
        After flipping, the maximum number of consecutive 1s is 4.
"""


def findMaxConsecutiveOnes(nums: list[int]) -> int:
    """
    Given a binary array, find the maximum number of consecutive 1s in this array if you can flip at most one 0.

    Input: [1,0,1,1,0]
    Output: 4
    Explanation: Flip the first zero will get the the maximum number of consecutive 1s.
    After flipping, the maximum number of consecutive 1s is 4.
    """
    if not nums or len(nums) == 0:
        return 0

    zero_val_indexes = []
    for i, v in enumerate(nums):
        if v == 0:
            zero_val_indexes.append(i)

    curr_max = len(nums) if len(zero_val_indexes) == 0 else 0
    print(zero_val_indexes)
    for i, v in enumerate(zero_val_indexes):
        start = 0 if i == 0 else zero_val_indexes[i - 1] + 1
        end = len(nums) if i + 1 >= len(zero_val_indexes) else zero_val_indexes[i + 1]
        length = len(range(start, end))
        print(start, end, length)
        if length > curr_max:
            curr_max = length
    return curr_max


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to findMaxConsecutiveOnes
    print(findMaxConsecutiveOnes([]))
