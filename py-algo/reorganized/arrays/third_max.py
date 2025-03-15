"""
Max

Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number.
        The time complexity must be in O(n).

        Input: [3, 2, 1]
        Output: 1
        Explanation: The third maximum is 1.

        Input: [2, 2, 3, 1]
        Output: 1
        Explanation: Note that the third maximum here means the third maximum distinct number.
                     Both numbers with value 2 are both considered as second maximum.
"""
def thirdMax(nums: list[int]) -> int:
        """
        Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number.
        The time complexity must be in O(n).

        Input: [3, 2, 1]
        Output: 1
        Explanation: The third maximum is 1.

        Input: [2, 2, 3, 1]
        Output: 1
        Explanation: Note that the third maximum here means the third maximum distinct number.
                     Both numbers with value 2 are both considered as second maximum.
        """

        max_set = set()
        max_set.add(nums[0])
        curr_max = nums[0]
        for n in nums:
            if n > curr_max or len(max_set) < 3:
                max_set.add(n)

            if len(max_set) > 3:
                max_set.remove(min(max_set))

        if len(max_set) == 3:
            return min(max_set)
        else:
            return max(max_set)


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to thirdMax
    print(thirdMax([]))
