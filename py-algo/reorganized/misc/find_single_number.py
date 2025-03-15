"""
Find_single_number

"""


def find_single_number(arr):
    num = 0
    for i in arr:
        num ^= i
    return num


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to find_single_number
    print(find_single_number([]))
