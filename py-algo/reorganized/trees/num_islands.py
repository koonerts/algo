"""
Islands

"""
def numIslands(grid: list[list[str]]) -> int:
        LAND, WATER = '1', '0'
        rows, cols = len(grid), len(grid[0])
        cnt = 0
def sink_island(row, col):
            if not (0 <= row < rows) or not (0 <= col < cols) or grid[row][col] == WATER:
                return

            grid[row][col] = WATER
            sink_island(row, col+1)
            sink_island(row, col-1)
            sink_island(row+1, col)
            sink_island(row-1, col)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == LAND:
                    cnt += 1
                    sink_island(r, c)

        for row in grid:
            print(row)

        return cnt


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to numIslands
    print(numIslands([]))
