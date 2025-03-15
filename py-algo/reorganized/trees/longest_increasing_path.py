"""
Increasing Path

"""
def longestIncreasingPath(matrix: list[list[int]]) -> int:
        if not matrix: return 0
def traverse(i, j, prev):
            nonlocal max_increasing_path_len

            if 0 <= i < len(matrix) and 0 <= j < len(matrix[0]) and (matrix[i][j] > prev or prev == float('-inf')):
                if memo[i][j] == float('-inf'):
                    left = traverse(i, j+1, matrix[i][j]) + 1
                    right = traverse(i, j-1, matrix[i][j]) + 1
                    up = traverse(i+1, j, matrix[i][j]) + 1
                    down = traverse(i-1, j, matrix[i][j]) + 1
                    memo[i][j] = max(left, right, up, down)

                max_increasing_path_len = max(max_increasing_path_len, memo[i][j])
                return memo[i][j]
            else:
                return 0

        max_increasing_path_len = 0
        memo = [[float('-inf') for j in range(len(matrix[0]))] for i in range(len(matrix))]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                traverse(i, j, float('-inf'))
        return max_increasing_path_len


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to longestIncreasingPath
    print(longestIncreasingPath([]))
