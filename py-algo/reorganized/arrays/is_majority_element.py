"""
Majority Element

"""
def isMajorityElement(nums: list[int], target: int) -> bool:
        if not nums: return False
def binary_search_low():
            low = -1
            start, end = 0, len(nums) - 1
            while start <= end:
                mid = (start + end) // 2
                if nums[mid] == target:
                    low = mid
                    end = mid - 1
                elif nums[mid] > target:
                    end = mid - 1
                else:
                    start = mid + 1
            return low
def binary_search_high():
            high = -1
            start, end = 0, len(nums) - 1
            while start <= end:
                mid = (start + end) // 2
                if nums[mid] == target:
                    high = mid
                    start = mid + 1
                elif nums[mid] > target:
                    end = mid - 1
                else:
                    start = mid + 1
            return high

        lower = binary_search_low()
        if lower == -1: return False
        higher = binary_search_high()

        cnt = higher - lower + 1
        return cnt > len(nums) / 2


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to isMajorityElement
    print(isMajorityElement([]))
