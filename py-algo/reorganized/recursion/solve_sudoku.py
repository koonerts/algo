"""
Solve Sudoku

Write a function to solve a Sudoku puzzle by filling the empty cells.
A sudoku solution must satisfy all of the following rules:
- Each of the digits 1-9 must occur exactly once in each row.
- Each of the digits 1-9 must occur exactly once in each column.
- Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.

Example:
    Input: board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    Output: The solved board

Time Complexity: O(9^(m*n)) where m and n are the dimensions of the board (typically 9x9)
Space Complexity: O(m*n) for the recursion stack
"""


class Solution:
    board = None
    rows = None
    cols = None
    boxes = None


def solveSudoku(board):
    """
    Solve a Sudoku puzzle by filling the empty cells.
    
    Args:
        board (List[List[str]]): 9x9 Sudoku board with '.' for empty cells
        
    Returns:
        None: The board is modified in-place
    """
    Solution.board = board
    Solution.rows = [[False for _ in range(9)] for _ in range(9)]
    Solution.cols = [[False for _ in range(9)] for _ in range(9)]
    Solution.boxes = [[False for _ in range(9)] for _ in range(9)]
    
    def can_place(row, col, val):
        return not Solution.rows[row][val-1] and not Solution.cols[col][val-1] and not Solution.boxes[row//3 * 3 + col//3][val-1]
    
    def place(row, col, val):
        val = int(val)
        Solution.rows[row][val-1] = True
        Solution.cols[col][val-1] = True
        Solution.boxes[row//3 * 3 + col//3][val-1] = True
        Solution.board[row][col] = str(val)
    
    def remove(row, col):
        val = int(Solution.board[row][col])
        Solution.rows[row][val-1] = False
        Solution.cols[col][val-1] = False
        Solution.boxes[row//3 * 3 + col//3][val-1] = False
        Solution.board[row][col] = '.'

    # Initialize the constraints based on existing digits
    for i in range(9):
        for j in range(9):
            if Solution.board[i][j] != '.':
                place(i, j, Solution.board[i][j])
    
    def dfs(row, col):
        if row >= 8 and col >= 9:
            return True
        elif col >= 9:
            return dfs(row+1, 0)
        elif Solution.board[row][col] != '.':
            return dfs(row, col+1)

        for i in range(1, 10):
            if can_place(row, col, i):
                place(row, col, i)
                is_solved = dfs(row, col+1)
                if is_solved:
                    return True
                remove(row, col)
        return False

    dfs(0, 0)
    return board


# Example usage
if __name__ == "__main__":
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    solved_board = solveSudoku(board)
    
    # Print the solved board
    for row in solved_board:
        print(" ".join(row))