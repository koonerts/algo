def letter_combinations(digits):
    """
    Given a string containing digits from 2 to 9 inclusive, with the possibility of each digit appearing multiple times, return all possible letter combinations that the number could represent. Return the answer in any order.
    The illustration below shows the mapping of digits to letters in a telephone dial pad.
    """
    if not digits:
        return []

    digit_to_char = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
    }

    def backtrack(index, current_combination):
        if len(current_combination) == len(digits):
            result.append(current_combination[:])
            return

        for char in digit_to_char[digits[index]]:
            current_combination.append(char)
            backtrack(index + 1, current_combination)
            current_combination.pop()

    result = []
    backtrack(0, [])
    return result
