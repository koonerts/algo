"""
Brackets

"""


def balancedBrackets(string):
    bracket_map = {"}": "{", "]": "[", ")": "("}
    open_brackets = {"{", "[", "("}
    stk = []
    for c in string:
        if c not in bracket_map and c not in open_brackets:
            continue
        elif c not in bracket_map:
            stk.append(c)
        else:
            if not stk or stk[-1] != bracket_map[c]:
                return False
            stk.pop()
    return len(stk) == 0


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to balancedBrackets
    print(balancedBrackets([]))
