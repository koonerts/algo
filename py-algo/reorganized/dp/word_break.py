"""
Break

"""


from collections import defaultdict
def wordBreak(s: str, wordDict: List[str]) -> List[str]:
    wordSet = set(wordDict)
    # table to map a string to its corresponding words break
    # {string: [['word1', 'word2'...], ['word3', 'word4', ...]]}
    memo = defaultdict(list)

    # @lru_cache(maxsize=None)    # alternative memoization solution
def _wordBreak_topdown(s):
        """ return list of word lists """
        if not s:
            return [[]]  # list of empty list

        if s in memo:
            return memo[s]

        for endIndex in range(1, len(s) + 1):
            word = s[:endIndex]
            if word in wordSet:
                # move forwards to break the postfix into words
                for subsentence in _wordBreak_topdown(s[endIndex:]):
                    print(word, subsentence)
                    memo[s].append([word] + subsentence)
        return memo[s]

    # break the input string into lists of words list
    _wordBreak_topdown(s)

    print(memo)
    # chain up the lists of words into sentences.
    return [" ".join(words) for words in memo[s]]



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to wordBreak
    print(wordBreak([]))
