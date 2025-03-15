"""
Number

"""


def singleNumber(nums: list[int]) -> int:
    xor = 0
    for num in nums:
        xor ^= num
    return xor


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to singleNumber
    print(singleNumber([]))
