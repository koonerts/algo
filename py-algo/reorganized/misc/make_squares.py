"""
Make_squares

Given a sorted array, create a new array containing squares of all the number of the input array in the sorted order.

    Example 1:
    Input: [-2, -1, 0, 2, 3]
    Output: [0, 1, 4, 4, 9]

    Example 2:
    Input: [-3, -1, 0, 1, 2]
    Output: [0 1 1 4 9]
"""


def make_squares(arr: list[int]) -> list[int]:
    """
    Given a sorted array, create a new array containing squares of all the number of the input array in the sorted order.

    Example 1:
    Input: [-2, -1, 0, 2, 3]
    Output: [0, 1, 4, 4, 9]

    Example 2:
    Input: [-3, -1, 0, 1, 2]
    Output: [0 1 1 4 9]
    """
    squares = []
    desc, asc = 0, 0
    while desc < len(arr) and arr[desc] < 0:
        desc += 1
    asc = desc + 1

    while len(squares) != len(arr):
        if desc < 0:
            squares.append(arr[asc] ** 2)
            asc += 1
        elif asc >= len(arr):
            squares.append(arr[desc] ** 2)
            desc -= 1
        else:
            if abs(arr[desc]) <= abs(arr[asc]):
                squares.append(arr[desc] ** 2)
                desc -= 1
            else:
                squares.append(arr[asc] ** 2)
                asc += 1

    return squares


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to make_squares
    print(make_squares([]))
