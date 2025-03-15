"""
Valid Sudoku

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules: Each row must contain the digits 1-9 without repetition, each column must contain the digits 1-9 without repetition, and each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Example:
    Input: [
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
    Output: true
    
Time Complexity: O(1) since the board size is fixed (9x9)
Space Complexity: O(1) since we use fixed-size data structures
"""

from typing import List

def isValidSudoku(board: List[List[str]]) -> bool:
    """
    Determine if a 9 x 9 Sudoku board is valid according to the following rules:
    - Each row must contain digits 1-9 without repetition
    - Each column must contain digits 1-9 without repetition
    - Each 3x3 sub-box must contain digits 1-9 without repetition
    
    Args:
        board (List[List[str]]): 9x9 Sudoku board
        
    Returns:
        bool: True if the board is valid, False otherwise
        
    Time Complexity: O(1) since the board size is fixed (9x9)
    Space Complexity: O(1) since we use fixed-size data structures
    """
    # Initialize sets to track numbers in each row, column, and 3x3 box
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    
    # Check each cell in the board
    for i in range(9):
        for j in range(9):
            # Skip empty cells
            if board[i][j] == '.':
                continue
                
            # Get the current value
            value = board[i][j]
            
            # Calculate which 3x3 box this cell belongs to (0-8)
            box_index = (i // 3) * 3 + (j // 3)
            
            # Check if value already exists in row, column, or box
            if (value in rows[i] or
                value in cols[j] or
                value in boxes[box_index]):
                return False
                
            # Add value to respective row, column, and box sets
            rows[i].add(value)
            cols[j].add(value)
            boxes[box_index].add(value)
    
    # If no conflicts were found, the board is valid
    return True




# Example usage
if __name__ == "__main__":
    isValidSudoku([
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
])  # Output: True
    isValidSudoku([
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
])  # Output: False (duplicated 8 in first column)
