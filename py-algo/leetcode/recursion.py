import numpy as np


def print_slice(arr):
    print(np.array(arr))

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print_list(self):
        vals = ''
        node = self
        while node:
            if node:
                vals += str(node.val)
            if node.next:
                vals += '->'
            node = node.next

        print(vals)


class Solution:

    def solveSudoku(self, board):
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


    def partition(self, s):
        results = []
        n = len(s)

        def isPalindrome(str_val):
            if len(str_val) == 0:
                return False
            lo, hi = 0, len(str_val)-1
            while lo < hi:
                if str_val[lo] != str_val[hi]:
                    return False
                lo += 1
                hi -= 1
            return True

        def dfs(idx, curr_str, curr_path):
            if idx >= len(s) and curr_str == '':
                results.append(curr_path.copy())
                return
            elif idx >= len(s):
                return

            for i in range(idx+1, n+1):
                if isPalindrome(s[idx:i]):
                    curr_path.append(curr_str + s[idx:i])
                    dfs(i, '', curr_path)
                    curr_path.pop()

        dfs(0, "", [])
        return results


    def reverseString(self, s: list[str]) -> None:
        """
        Write a function that reverses a string. The input string is given as an array of characters char[].
        Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
        """
        l, r = 0, len(s)-1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

    def exist(self, board: list[list[str]], word: str) -> bool:
        if not word or not board: return False

        def search(x, y, word_idx, visited) -> bool:
            if x < 0 or y < 0 or x >= len(board) or y >= len(board[x]) or board[x][y] != word[word_idx] or (x, y) in visited:
                return False
            else:
                if word_idx == len(word)-1:
                    return True
                else:
                    visited.add((x, y))
                    return search(x, y-1, word_idx+1, visited.copy()) or \
                           search(x, y+1, word_idx+1, visited.copy()) or \
                           search(x-1, y, word_idx+1, visited.copy()) or \
                           search(x+1, y, word_idx+1, visited.copy())

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    if search(i, j, 0, set()):
                        return True
        return False

    def swapPairs(self, head: ListNode) -> ListNode:
        if not head.next: return head

        def swap_rec(node, prev, prev_sublist_tail, k):
            if not node:
                if prev_sublist_tail and prev and (prev_sublist_tail != prev):
                    prev_sublist_tail.next = prev
                if prev:
                    prev.next = None
            else:
                if k == 1:
                    temp = node.next
                    node.next = prev
                    if prev_sublist_tail:
                        prev_sublist_tail.next = node
                    swap_rec(temp, prev, prev, (k+1) % 2)
                else:
                    swap_rec(node.next, node, prev_sublist_tail, (k+1) % 2)

        new_head = head.next
        swap_rec(head, prev=None, prev_sublist_tail=head, k=0)
        return new_head

    def totalNQueens(self, n):
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


board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
print(Solution().solveSudoku(board))
