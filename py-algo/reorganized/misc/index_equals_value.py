"""
Equals Value

"""
def indexEqualsValue(array):
    lo, hi = 0, len(array) - 1

    while lo <= hi:
        mid = (lo+hi)//2
        if array[mid] == mid:
            return mid
        # elif



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to indexEqualsValue
    print(indexEqualsValue([]))
