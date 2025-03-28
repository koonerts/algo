from collections import deque


def find_subsets(nums: list[int]):
    """
    Given a set with distinct elements, find all of its distinct subsets.

    Example 1:
    Input: [1, 3]
    Output: [], [1], [3], [1,3]

    Example 2:
    Input: [1, 5, 3]
    Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3]
    """
    subsets = [[]]

    for num in nums:
        for i in range(len(subsets)):
            subsets.append(list(subsets[i]) + [num])
    return subsets


def find_subsets_with_dups(nums: list[int]):
    """
    Given a set of numbers that might contain duplicates, find all of its distinct subsets.

    Example 1:
    Input: [1, 3, 3]
    Output: [], [1], [3], [1,3], [3,3], [1,3,3]

    Example 2:
    Input: [1, 5, 3, 3]
    Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3], [3,3], [1,3,3], [3,3,5], [1,5,3,3]
    """
    if not nums:
        return [[]]

    nums.sort()
    subsets = [[]]
    start, end = 0, 0

    for i, num in enumerate(nums):
        start = 0
        if i > 0 and nums[i - 1] == nums[i]:
            start = end + 1
        end = len(subsets) - 1
        for j in range(start, end + 1):
            subsets.append(subsets[j] + [num])
    return subsets


def find_permutations(nums: list[int]):
    """
    Given a set of distinct numbers, find all of its permutations.
    Permutation is defined as the re-arranging of the elements of the set.
    For example, {1, 2, 3} has the following six permutations:

    {1, 2, 3}
    {1, 3, 2}
    {2, 1, 3}
    {2, 3, 1}
    {3, 1, 2}
    {3, 2, 1}

    If a set has ‘n’ distinct elements it will have n! permutations.

    Example 1:
    Input: [1,3,5]
    Output: [1,3,5], [1,5,3], [3,1,5], [3,5,1], [5,1,3], [5,3,1]
    """
    if not nums:
        return []
    result = []
    q: deque[list[int]] = deque()

    for i, num in enumerate(nums):
        if i == 0:
            q.append([num])
            continue

        q_len = len(q)
        for _ in range(q_len):
            set_ = q.popleft()
            for j in range(len(set_) + 1):
                set_copy = list(set_)
                set_copy.insert(j, num)

                if len(set_copy) == len(nums):
                    result.append(set_copy)
                else:
                    q.append(set_copy)

    return result


def find_letter_case_string_permutations(str_in: str) -> list[str]:
    """
    Given a string, find all of its permutations preserving the character sequence but changing case.

    Example 1:
    Input: "ad52"
    Output: "ad52", "Ad52", "aD52", "AD52"

    Example 2:
    Input: "ab7c"
    Output: "ab7c", "Ab7c", "aB7c", "AB7c", "ab7C", "Ab7C", "aB7C", "AB7C"
    """
    q = deque([""])
    for c in str_in:
        for _ in range(len(q)):
            current_permutation = q.popleft()
            if c.isalpha():
                q.append(current_permutation + c.lower())
                q.append(current_permutation + c.upper())
            else:
                q.append(current_permutation + c)
    return list(q)


def generate_valid_parentheses(N: int):
    """
    For a given number ‘N’, write a function to generate all combination of ‘N’ pairs of balanced parentheses.

    Example 1:
    Input: N=2
    Output: (()), ()()

    Example 2:
    Input: N=3
    Output: ((())), (()()), (())(), ()(()), ()()()
    """
    # TODO: Come back to
    result = []
    return result


def generate_generalized_abbreviation(word: str):
    """
    Given a word, write a function to generate all of its unique generalized abbreviations.
    Generalized abbreviation of a word can be generated by replacing each substring of the word by the
    count of characters in the substring.

    Take the example of “ab” which has four substrings:
        “”, “a”, “b”, and “ab”.

    After replacing these substrings in the actual word by the count of characters
    we get all the generalized abbreviations:
        “ab”, “1b”, “a1”, and “2”.

    Example 1:
    Input: "BAT"
    Output: "BAT", "BA1", "B1T", "B2", "1AT", "1A1", "2T", "3"

    Example 2:
    Input: "code"
    Output: "code", "cod1", "co1e", "co2", "c1de", "c1d1", "c2e", "c3", "1ode", "1od1", "1o1e", "1o2", "2de", "2d1", "3e", "4"
    """
    q = deque([""])

    for c in word:
        for _ in range(len(q)):
            permutation = q.popleft()
            q.append(permutation + c)

            if permutation and permutation[-1].isnumeric():
                i = -1
                while i - 1 >= -len(permutation) and permutation[i - 1].isnumeric():
                    i -= 1

                q.append(permutation[:i] + str(int(permutation[i:]) + 1))
            else:
                q.append(permutation + "1")

    return list(q)


def diff_ways_to_evaluate_expression(input: str) -> list[int]:
    """
    Given an expression containing digits and operations (+, -, *), find all possible ways in which the expression can be evaluated by grouping the numbers and operators using parentheses.

    Example 1:
    Input: "1+2*3"
    Output: 7, 9
    Explanation: 1+(2*3) => 7 and (1+2)*3 => 9

    Example 2:
    Input: "2*3-4-5"
    Output: 8, -12, 7, -7, -3
    Explanation: 2*(3-(4-5)) => 8, 2*(3-4-5) => -12, 2*3-(4-5) => 7, 2*(3-4)-5 => -7, (2*3)-4-5 => -3
    """
    # TODO: Come back to
    result = []
    return result


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def find_unique_trees(n: int):
    """
    Given a number ‘n’, write a function to return all structurally unique Binary Search Trees (BST) that can store values 1 to ‘n’.
    """
    # TODO: Come back to
    pass


def count_trees(n):
    """
    Given a number ‘n’, write a function to return the count of structurally unique Binary Search Trees (BST) that can store values 1 to ‘n’.

    Example 1:
    Input: 2
    Output: 2
    Explanation: As we saw in the previous problem, there are 2 unique BSTs storing numbers from 1-2.

    Example 2:
    Input: 3
    Output: 5
    Explanation: There will be 5 unique BSTs that can store numbers from 1 to 3.
    """
    # TODO: Come back to
    count = -1
    return count


def main():
    print("Total trees: " + str(count_trees(2)))
    print("Total trees: " + str(count_trees(3)))


main()
