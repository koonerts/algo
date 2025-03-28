"""
Evaluate Reverse Polish Notation

Problems is to evaluate an expression in Reverse Polish Notation.
Valid operators are +, -, *, and /. Each operand may be an integer or another expression.
"""


def evalRPN(arr):
    """
    Evaluates an expression in Reverse Polish Notation.

    Args:
        arr: List of strings representing the expression

    Returns:
        int: Result of evaluating the expression
    """
    stk = []
    ops = {"+", "*", "/", "-"}
    for i, val in enumerate(arr):
        if val in ops:
            n1, n2 = stk.pop(), stk.pop()
            stk.append(str(eval(n2 + val + n1)))
        else:
            stk.append(val)
    return int(float(stk[-1]))


# Example usage
if __name__ == "__main__":
    print(evalRPN(["2", "1", "+", "3", "*"]))  # Output: 9
    print(evalRPN(["4", "13", "5", "/", "+"]))  # Output: 6
