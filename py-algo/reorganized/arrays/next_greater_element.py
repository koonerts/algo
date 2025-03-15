"""
Greater Element

"""


import collections
from collections import defaultdict
def nextGreaterElement(nums1: list[int], nums2: list[int]) -> list[int]:
        stack = []
        next_number = collections.defaultdict(lambda: -1)

        for num in nums2:
            while stack and num > stack[-1]:
                next_number[stack.pop()] = num
            stack.append(num)

        return list(map(lambda x: next_number[x], nums1))


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to nextGreaterElement
    print(nextGreaterElement([]))
