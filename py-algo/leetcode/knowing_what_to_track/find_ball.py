"""
Ball

"""


def findBall(grid: list[list[int]]) -> list[int]:
    LEFT, RIGHT = -1, 1
    ret = [-1] * len(grid[0])

    def traverse(x, y) -> int:
        if (
            0 <= x < len(grid)
            and 0 <= y < len(grid[0])
            and grid[x][y] != -1
            and grid[x][y] != 1
        ):
            return grid[x][y]
        elif x > len(grid) - 1:
            return y * 10
        elif (
            grid[x][y] == LEFT
            and y == 0
            or grid[x][y] == RIGHT
            and y == len(grid[0]) - 1
            or grid[x][y] == RIGHT
            and grid[x][y + 1] == LEFT
            or grid[x][y] == LEFT
            and grid[x][y - 1] == RIGHT
        ):
            return -1
        else:
            grid[x][y] = traverse(x + 1, y + grid[x][y])
            return grid[x][y]

    for i in range(len(ret)):
        ret[i] = traverse(0, i) // 10
    return ret


# Example usage
if __name__ == "__main__":
    # Example calls to findBall
    print(findBall([]))
