"""
Number Sum

"""
def fourNumberSum(array, targetSum):
    if len(array) < 4: return []

    result = []
    array.sort()
    for i in range(len(array)-3):
        for j in range(i+1, len(array)-2):
            k, l = j+1, len(array)-1
            
            while k < l:
                val = array[i] + array[j] + array[k] + array[l]
                if val == targetSum:
                    result.append([array[i], array[j], array[k], array[l]])
                    k += 1
                    l -= 1
                elif val < targetSum:
                    k += 1
                else:
                    l -= 1
    return result



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to fourNumberSum
    print(fourNumberSum([]))
