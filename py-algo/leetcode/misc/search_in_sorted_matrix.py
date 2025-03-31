"""
In Sorted Matrix

"""


def searchInSortedMatrix(matrix, target):
    row, col = len(matrix) - 1, 0
    while row >= 0 and col < len(matrix[0]):
        if matrix[row][col] > target:
            row -= 1
        elif matrix[row][col] < target:
            col += 1
        else:
            return [row, col]
    return [-1, -1]


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to searchInSortedMatrix
    print(searchInSortedMatrix([]))
