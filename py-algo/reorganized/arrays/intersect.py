"""
Intersect

"""


import collections
from collections import Counter
def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
        if len(nums2) < len(nums1):
            return self.intersect(nums2, nums1)

        n2_freq = collections.Counter(nums2)
        result = []
        for i in range(len(nums1)):
            if nums1[i] in n2_freq:
                result.append(nums1[i])
                if n2_freq[nums1[i]] == 1:
                    del n2_freq[nums1[i]]
                else:
                    n2_freq[nums1[i]] -= 1
        return result


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to intersect
    print(intersect([]))
