"""
Exist

"""
def exist(board: list[list[str]], word: str) -> bool:
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


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to exist
    print(exist([]))
