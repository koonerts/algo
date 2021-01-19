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


print(Solution().totalNQueens(4))
