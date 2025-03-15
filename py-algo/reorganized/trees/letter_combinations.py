"""
Combinations

"""
def letterCombinations(digits: str) -> list[str]:
    phone = {'2': ['a', 'b', 'c'],
                '3': ['d', 'e', 'f'],
                '4': ['g', 'h', 'i'],
                '5': ['j', 'k', 'l'],
                '6': ['m', 'n', 'o'],
                '7': ['p', 'q', 'r', 's'],
                '8': ['t', 'u', 'v'],
                '9': ['w', 'x', 'y', 'z']}
    results = []
    def dfs(curr_str, digit_index):
        if len(curr_str) == len(digits):
            results.append(curr_str)
        else:
            for letter in phone[digits[digit_index]]:
                dfs(curr_str+letter, digit_index+1)

    dfs('', 0)
    return results


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to letterCombinations
    print(letterCombinations([]))
