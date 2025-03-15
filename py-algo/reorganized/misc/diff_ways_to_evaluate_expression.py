"""
Diff_ways_to_evaluate_expression

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



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to diff_ways_to_evaluate_expression
    print(diff_ways_to_evaluate_expression([]))
