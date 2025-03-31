"""
Rotate

"""


def rotate(nums: list[int], k: int) -> None:
    if not nums or k == 0:
        return

    k = k % len(nums)
    idx, prev, temp = 0, nums[0], 0
    for _ in range(len(nums)):
        idx = (idx + k) % len(nums)
        temp = nums[idx]
        nums[idx] = prev
        prev = temp


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to rotate
    print(rotate([]))
