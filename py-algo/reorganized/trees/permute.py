"""
Permute

"""


from collections import deque
def permute(nums: list[int]) -> list[list[int]]:
        if not nums or len(nums) == 1: return []

        res = []
        q = deque([[]])
        for i in range(0, len(nums)):
            curr = q.popleft()
            for j in range(len(curr)+1):
                copy_curr = curr.copy()
                copy_curr.insert(j, nums[i])

                if len(copy_curr) < len(nums):
                    q.append(copy_curr)
                else:
                    res.append(copy_curr)
        return res


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to permute
    print(permute([]))
