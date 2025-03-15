"""
Sum Closest

"""


def threeSumClosest(nums: list[int], target: int) -> int:
    if len(nums) == 3:
        return sum(nums)

    nums.sort()
    closest_sum = float("inf")
    for i in range(len(nums)):
        left, right = i + 1, len(nums) - 1
        while left < right:
            curr_sum = nums[i] + nums[left] + nums[right]
            if curr_sum == target:
                return curr_sum
            else:
                if abs(curr_sum - target) < abs(closest_sum - target):
                    closest_sum = curr_sum

                if curr_sum < target:
                    left += 1
                else:
                    right -= 1
    return closest_sum


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to threeSumClosest
    print(threeSumClosest([]))
