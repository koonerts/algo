"""
Sum

"""
def twoSum(numbers: list[int], target: int) -> list[int]:
        start, end = 0, len(numbers) - 1
        while start < end:
            val = numbers[start] + numbers[end]
            if val == target:
                return [start + 1, end + 1]
            elif val > target:
                end -= 1
            else:
                start += 1


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to twoSum
    print(twoSum([]))
