"""
Missing Ranges

"""
def findMissingRanges(nums: list[int], lower: int, upper: int) -> list[str]:
        if lower == upper and lower not in nums:
            return [str(lower)]
        elif not nums:
            return [f'{lower}->{upper}']

        result = []
        for i, num in enumerate(nums):
            if i == 0:
                if lower < num:
                    if lower + 1 == num:
                        result.append(str(lower))
                    else:
                        result.append(f'{lower}->{num - 1}')
            else:
                diff = num - nums[i - 1]
                if diff == 2:
                    result.append(str(num - 1))
                elif diff > 2:
                    result.append(f'{nums[i - 1] + 1}->{num - 1}')

            if i == len(nums) - 1 and num < upper:
                if num + 1 == upper:
                    result.append(str(upper))
                else:
                    result.append(f'{num + 1}->{upper}')
        return result


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to findMissingRanges
    print(findMissingRanges([]))
