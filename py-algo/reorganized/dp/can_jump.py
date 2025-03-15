"""
Jump

"""
def canJump(nums: list[int]) -> bool:
        if len(nums) <= 1: return True

        target_index = len(nums) - 1
        left_index = len(nums) - 2

        while left_index >= 0:
            dist = target_index - left_index
            if nums[left_index] >= dist:
                target_index = left_index
            left_index -= 1
        return target_index == 0


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to canJump
    print(canJump([]))
