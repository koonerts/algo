def three_sum(nums: list[int]) -> list[list[int]]:
    """
    Three Sum

    Given an array of integers, find all unique triplets in the array that give the sum of zero.

    Example:
        Input: [-1, 0, 1, 2, -1, -4]
        Output: [[-1, -1, 2], [-1, 0, 1]]

    Time Complexity: O(n²) where n is the length of the array (due to sorting + nested loops)
    Space Complexity: O(1) or O(n) depending on sort implementation (ignoring space for result)
    """
    result: list[list[int]] = []
    n: int = len(nums)

    if n < 3:
        return result

    nums.sort()

    for i in range(n - 2):
        # Skip duplicate values for the first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left: int = i + 1
        right: int = n - 1
        target: int = -nums[i] # Target for the sum of the remaining two elements

        while left < right:
            current_sum: int = nums[left] + nums[right]

            if current_sum == target:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                # Skip duplicate values for the second and third elements
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif current_sum < target:
                left += 1 # Need a larger sum
            else: # current_sum > target
                right -= 1 # Need a smaller sum

    return result

