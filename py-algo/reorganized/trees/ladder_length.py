"""
Length

"""


import collections
from collections import deque
def ladderLength(beginWord: str, endWord: str, wordList: list[str]) -> int:
        q = collections.deque([beginWord])
        visited = set()
        word_set = set(wordList)

        ladder_len = 0
        while q:
            ladder_len += 1
            for _ in range(len(q)):
                curr_word = q.popleft()
                if curr_word == endWord:
                    return ladder_len
                else:
                    visited.add(curr_word)
                    for word in (w for w in word_set-visited):
                        char_diff = 0
                        for i in range(len(word)):
                            if word[i] != curr_word[i]:
                                char_diff += 1
                                if char_diff > 1: break
                        if char_diff == 1:
                            q.append(word)
        return 0


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to ladderLength
    print(ladderLength([]))
