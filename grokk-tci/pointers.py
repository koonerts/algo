

def pair_with_targetsum(arr: list[int], target_sum: int) -> list[int]:
    """
    Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.
    Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.

    Example 1:
    Input: [1, 2, 3, 4, 6], target=6
    Output: [1, 3]
    Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6

    Example 2:
    Input: [2, 5, 9, 11], target=11
    Output: [0, 2]
    Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11
    """
    start, end = 0, len(arr) - 1
    while start < end:
        sum_ = arr[start] + arr[end]
        if sum_ == target_sum:
            return [start, end]
        elif sum_ > target_sum:
            end -= 1
        else:
            start += 1

    return [-1, -1]


def remove_duplicates(arr: list[int]) -> int:
    """
    Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space.
    After removing the duplicates in-place return the length of the subarray that has no duplicate in it.

    Example 1:
    Input: [2, 3, 3, 3, 6, 9, 9]
    Output: 4
    Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].

    Example 2:
    Input: [2, 2, 2, 11]
    Output: 2
    Explanation: The first two elements after removing the duplicates will be [2, 11].
    """
    switch_index, i = 1, 1

    while i < len(arr):
        if arr[switch_index - 1] != arr[i]:
            arr[switch_index] = arr[i]
            switch_index += 1
        i += 1

    print(arr)
    return switch_index


def make_squares(arr: list[int]) -> list[int]:
    """
    Given a sorted array, create a new array containing squares of all the number of the input array in the sorted order.

    Example 1:
    Input: [-2, -1, 0, 2, 3]
    Output: [0, 1, 4, 4, 9]

    Example 2:
    Input: [-3, -1, 0, 1, 2]
    Output: [0 1 1 4 9]
    """
    squares = []
    desc, asc = 0, 0
    while desc < len(arr) and arr[desc] < 0:
        desc += 1
    asc = desc + 1

    while len(squares) != len(arr):
        if desc < 0:
            squares.append(arr[asc]**2)
            asc += 1
        elif asc >= len(arr):
            squares.append(arr[desc]**2)
            desc -= 1
        else:
            if abs(arr[desc]) <= abs(arr[asc]):
                squares.append(arr[desc]**2)
                desc -= 1
            else:
                squares.append(arr[asc]**2)
                asc += 1

    return squares


def search_triplets(arr: list[int]) -> list[list[int]]:
    """
    Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

    Example 1:
    Input: [-3, 0, 1, 2, -1, 1, -2]
    Output: [[-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]]
    Explanation: There are four unique triplets whose sum is equal to zero.

    Example 2:
    Input: [-5, 2, -1, -2, 3]
    Output: [[-5, 2, 3], [-2, -1, 3]]
    Explanation: There are two unique triplets whose sum is equal to zero.
    """
    triplets = []

    # time: O(nlog(n))
    # space: O(n)
    arr.sort()

    # time: O(n^2) -> loop through each index and nested loop through i+i..i+n-1 to n
    # space: O(n) -> triplets
    for i, val in enumerate(arr):
        start = i + 1
        end = len(arr) - 1
        while start < end:
            sum_ = arr[start] + arr[end] + val
            if sum_ == 0:
                triplets.append([val, arr[start], arr[end]])
                end = len(arr) - 1

                # handle duplicates in the array by incrementing start by 1 until we get a non-duplicate start
                while True:
                    start += 1
                    if start > len(arr) or arr[start] != arr[start -1]:
                        break

            elif sum_ > 0:
                end -= 1
            else:
                start += 1
    """
    Overall time complexity is O(nlogn + n^2) -> O(n^2)
    Overall space complexity is O(n + n) -> O(n)
    """
    return triplets


def triplet_sum_close_to_target(arr: list[int], target_sum: int):
    """
    Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close to the target number as possible and
    return the sum of the triplet. If there are more than one such triplet, return the sum of the triplet with the smallest sum.

    Example 1:
    Input: [-2, 0, 1, 2], target=2
    Output: 1
    Explanation: The triplet [-2, 1, 2] has the closest sum to the target.

    Example 2:
    Input: [-3, -1, 1, 2], target=1
    Output: 0
    Explanation: The triplet [-3, 1, 2] has the closest sum to the target.

    Example 3:
    Input: [1, 0, 1, 1], target=100
    Output: 3
    Explanation: The triplet [1, 1, 1] has the closest sum to the target.
    """
    # time: O(nlogn)
    # space: O(n)
    arr.sort()
    closest_sum: int = 0

    # time: O(n^2)
    # space: O(1)
    for i, val in enumerate(arr):
        start = i+1
        end = len(arr) - 1
        while start < end:
            sum_ = val + arr[start] + arr[end]
            if sum_ == target_sum:
                return 0
            elif sum_ < target_sum:
                start += 1
            else:
                end -= 1

            diff = abs(target_sum - sum_)
            if diff < abs(target_sum - closest_sum):
                closest_sum = sum_
            elif diff == abs(target_sum - closest_sum):
                closest_sum = min(closest_sum, sum_)

    """
    Overall time: O(nlogn + n^2) -> O(n^2)
    Overall space: O(n)
    """
    return closest_sum


def triplet_with_smaller_sum(arr: list[int], target: int) -> int:
    """
    Given an array arr of unsorted numbers and a target sum, count all triplets in it
    such that arr[i] + arr[j] + arr[k] < target where i, j, and k are three different indices.
    Write a function to return the count of such triplets.

    Example 1:
    Input: [-1, 0, 2, 3], target=3
    Output: 2
    Explanation: There are two triplets whose sum is less than the target: [-1, 0, 3], [-1, 0, 2]

    Example 2:
    Input: [-1, 4, 2, 1, 3], target=5
    Output: 4
    Explanation: There are four triplets whose sum is less than the target: [-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]
    """

    count = -1
    return count


print(triplet_sum_close_to_target([1, 0, 1, 1], 100))