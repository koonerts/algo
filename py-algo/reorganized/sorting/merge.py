"""
Merge Sorted Array

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively. Merge nums1 and nums2 into a single array sorted in non-decreasing order. The final sorted array should be stored inside nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Example:
    Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
    Output: [1,2,2,3,5,6]
    
Time Complexity: O(m + n) where m and n are the lengths of the arrays
Space Complexity: O(1) as we modify nums1 in-place
"""

from typing import List

def merge(intervals: list[list[int]]) -> list[list[int]]:
    """
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively. Merge nums1 and nums2 into a single array sorted in non-decreasing order. The final sorted array should be stored inside nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Args:
    nums1 (List[int]): First sorted array with extra space
m (int): Number of elements in nums1
nums2 (List[int]): Second sorted array
n (int): Number of elements in nums2
    
Returns:
    None: nums1 is modified in-place
    
Time Complexity: O(m + n) where m and n are the lengths of the arrays
Space Complexity: O(1) as we modify nums1 in-place
"""
    if not intervals:
    return []

    start, end = 0, 1
    intervals.sort(key=lambda x: x[start])

    prev = intervals[0]
    result = [prev]
    for i in range(1, len(intervals)):
    curr = intervals[i]
    if prev[end] < curr[start]:
    result.append(curr)
    prev = curr
    else:
    prev[end] = max(prev[end], curr[end])
    return result




    # Example usage
    if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    merge(nums1, 3, nums2, 3)
    print(nums1)  # Output: [1, 2, 2, 3, 5, 6]




# Example usage
if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    merge(nums1, 3, nums2, 3)
    print(nums1)  # Output: [1, 2, 2, 3, 5, 6]
