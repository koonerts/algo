"""
Find_target_subsets

You are given a set of positive numbers and a target sum ‘S’. Each number should be assigned either a ‘+’ or ‘-’ sign. We need to find the total ways to assign symbols to make the sum of the numbers equal to the target ‘S’.

    Example 1:
    Input: {1, 1, 2, 3}, S=1
    Output: 3
    Explanation: The given set has '3' ways to make a sum of '1': {+1-1-2+3} & {-1+1-2+3} & {+1+1+2-3}

    Example 2:
    Input: {1, 2, 7, 1}, S=9
    Output: 2
    Explanation: The given set has '2' ways to make a sum of '9': {+1+2+7-1} & {-1+2+7+1}
"""


def find_target_subsets(nums, s):
    """
    You are given a set of positive numbers and a target sum ‘S’. Each number should be assigned either a ‘+’ or ‘-’ sign. We need to find the total ways to assign symbols to make the sum of the numbers equal to the target ‘S’.

    Example 1:
    Input: {1, 1, 2, 3}, S=1
    Output: 3
    Explanation: The given set has '3' ways to make a sum of '1': {+1-1-2+3} & {-1+1-2+3} & {+1+1+2-3}

    Example 2:
    Input: {1, 2, 7, 1}, S=9
    Output: 2
    Explanation: The given set has '2' ways to make a sum of '9': {+1+2+7-1} & {-1+2+7+1}
    """
    # TODO: Come back to
    return -1


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to find_target_subsets
    print(find_target_subsets([]))
