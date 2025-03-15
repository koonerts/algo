"""
Sudoku

"""
def solveSudoku(board):
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



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to solveSudoku
    print(solveSudoku([]))
