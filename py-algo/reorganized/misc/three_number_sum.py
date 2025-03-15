"""
Number Sum

"""
def threeNumberSum(array, targetSum):
    array.sort()

    res = []
    for i in range(len(array) - 1):
        j = i + 1
        k = len(array) - 1
        while j < k:
            sum_val = array[i] + array[j] + array[k]
            if sum_val == targetSum:
                res.append([array[i], array[j], array[k]])
                j += 1
                k -= 1
            elif sum_val < targetSum:
                j += 1
            else:
                k -= 1
    return res



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to threeNumberSum
    print(threeNumberSum([]))
