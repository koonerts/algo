from heapq import heappush, heappop
from collections import defaultdict

def median_sliding_window(nums: list[int], k: int) -> list[float]:
    """Problem: Sliding Window Median (Two Heaps with Lazy Deletion - Corrected)
    Statement

    Given an integer array, nums, and an integer, k, there is a sliding window of size k,
    which is moving from the very left to the very right of the array.

    We can only see the k numbers in the window.
    Each time the sliding window moves right by one position.

    Given this scenario, return the median of the each window.
    Answers within 10^-5 of the actual value will be accepted.

    Constraints:
        1 <= k <= nums.length <= 10^3
        -2^31 <= nums[i] <= 2^31 - 1
    """

    medians: list[float] = []
    # Max-heap for lower half (store negative values)
    lower_half: list[int] = []
    # Min-heap for upper half
    upper_half: list[int] = []
    # Hash map for lazy deletion: maps number to its count of invalid occurrences
    invalidated: defaultdict[int, int] = defaultdict(int)

    for i, num in enumerate(nums):
        # --- Removal Phase (if window is full) ---
        if i >= k:
            outgoing_num = nums[i - k]
            invalidated[outgoing_num] += 1

        # --- Balance factor: Tracks net additions/removals from heaps ---
        # +1 means lower_half is favoured, -1 means upper_half is favoured
        balance = 0

        # Determine which heap the outgoing element *would* belong to
        if i >= k:
            outgoing_num = nums[i - k]
            if lower_half and outgoing_num <= -lower_half[0]:
                 balance -= 1 # Conceptually removed from lower
            else:
                 balance += 1 # Conceptually removed from upper


        # --- Addition Phase ---
        # Add the new number initially favouring lower_half
        if not lower_half or num <= -lower_half[0]:
            heappush(lower_half, -num)
            balance += 1
        else:
            heappush(upper_half, num)
            balance -= 1


        # --- Re-balancing Phase ---
        # If lower_half gained net influence, move max element from lower to upper
        if balance > 0:
            heappush(upper_half, -heappop(lower_half))
        # If upper_half gained net influence, move min element from upper to lower
        if balance < 0:
            heappush(lower_half, -heappop(upper_half))


        # --- Pruning Phase (Remove invalid elements from heap tops) ---
        while lower_half and invalidated[-lower_half[0]] > 0:
            invalidated[-lower_half[0]] -= 1
            heappop(lower_half)
        while upper_half and invalidated[upper_half[0]] > 0:
            invalidated[upper_half[0]] -= 1
            heappop(upper_half)


        # --- Median Calculation Phase ---
        if i >= k - 1:
            if k % 2 == 1:
                # Odd k: median is the top of lower_half (max of lower half)
                median = float(-lower_half[0])
            else:
                # Even k: median is avg of top of lower_half and top of upper_half
                median = (-float(lower_half[0]) + float(upper_half[0])) / 2.0
            medians.append(median)

    return medians

