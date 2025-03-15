"""
Find_range2

"""
def find_range2(arr, key):
    result = [- 1, -1]
    result[0] = binary_search2(arr, key, False)
    if result[0] != -1:  # no need to search, if 'key' is not present in the input array
        result[1] = binary_search2(arr, key, True)
    return result



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to find_range2
    print(find_range2([]))
