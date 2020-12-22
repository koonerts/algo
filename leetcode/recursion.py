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


print(Solution().exist([["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]], 'ABCESEEEFS'))
