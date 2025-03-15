"""
Median Sorted Arrays

https://leetcode.com/problems/median-of-two-sorted-arrays/
"""
def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
        """
        https://leetcode.com/problems/median-of-two-sorted-arrays/
        """
        len1, len2 = len(nums1), len(nums2)
        if len2 < len1:
            return self.findMedianSortedArrays(nums2, nums1)

        total_len = len1 + len2
        start, end = 0, len1 - 1

        while True:
            p1 = (start + end) // 2
            p2 = ((total_len + 1) // 2) - (p1 + 2)

            n1_p_val = float('-inf') if p1 < 0 else nums1[p1]
            n2_p_val = float('-inf') if p2 < 0 else nums2[p2]
            n1_next_val = float('inf') if p1 + 1 >= len1 else nums1[p1 + 1]
            n2_next_val = float('inf') if p2 + 1 >= len2 else nums2[p2 + 1]

            if n1_p_val <= n2_next_val and n2_p_val <= n1_next_val:
                if total_len % 2 == 1:
                    return max(n1_p_val, n2_p_val)
                else:
                    return (max(n1_p_val, n2_p_val) + min(n1_next_val, n2_next_val)) / 2
            elif n1_p_val > n2_next_val:
                end = p1 - 1
            else:
                start = p1 + 1


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to findMedianSortedArrays
    print(findMedianSortedArrays([]))
