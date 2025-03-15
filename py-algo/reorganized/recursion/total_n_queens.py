"""
N Queens

"""
def totalNQueens(n):
        diag1 = [0 for i in range((2*n) - 1)]
        diag2 = [0 for i in range((2*n) - 1)]
        cols = [0 for i in range(n)]
        queens = []
        result = []
def can_place(row, col):
            return not cols[col] and not diag1[row-col] and not diag2[row+col]
def place_queen(row, col):
            queens.append((row, col))
            cols[col] = 1
            diag1[row-col] = 1
            diag2[row+col] = 1
def remove_queen(row, col):
            queens.remove((row,col))
            cols[col] = 0
            diag1[row-col] = 0
            diag2[row+col] = 0
def traverse(row=0):
            for col in range(n):
                if can_place(row, col):
                    place_queen(row, col)

                    if row == n-1:
                        board = []
                        for i in range(n):
                            string = ''
                            for j in range(n):
                                if (i,j) in queens:
                                    string += 'Q'
                                else:
                                    string += '.'
                            board.append(string)
                        result.append(board)
                    else:
                        traverse(row+1)
                    remove_queen(row, col)

        traverse()
        return result



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to totalNQueens
    print(totalNQueens([]))
