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

    # def exist(self, board: list[list[str]], word: str) -> bool:
    #
    #     def search(idx:int) -> bool:
    #         pass
    #
    #     char_idx_map = {}
    #     for i, c in enumerate(word):
    #         char_idx_map[c] = char_idx_map.get(c, [])
    #         char_idx_map[c].append(i)
    #
    #     for i in range(len(board)):
    #         for j in range(len(board[i])):
    #             if board[i][j] in char_idx_map:
    #                 for idx


root = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
root.print_list()
res = Solution().swapPairs(root)
res.print_list()

