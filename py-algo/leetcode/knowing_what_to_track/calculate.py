"""
Calculate

"""


def calculate(s: str) -> int:
    stk = []
    opening_paren_indexes = []

    for c in s:
        if c == ")":
            val = str(eval("".join(stk[opening_paren_indexes[-1] + 1 :])))
            while len(stk) > opening_paren_indexes[-1]:
                stk.pop()
            stk.append(val)
            opening_paren_indexes.pop()
        elif c == "(":
            stk.append(c)
            opening_paren_indexes.append(len(stk) - 1)
        else:
            stk.append(c)
    return eval("".join(stk))


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to calculate
    print(calculate([]))
