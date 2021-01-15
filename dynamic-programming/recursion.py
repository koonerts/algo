

def isSafe(i, j, board):
    for c in range(len(board)):
        for r in range(len(board)):
            if board[c][r] == 'q' and i==c and j!=r:
                return False
            elif board[c][r] == 'q' and j==r and i!=c:
                return False
            elif (i+j == c+r or i-j == c-r) and board[c][r] == 'q':
                return False
    return True


def placeNQueens(n, board):
    """
    To check whether index i,j is safe to place queen call isSafe(i, j, board)
    True means it is safe, False means it is not
    """
    