"""
R P N

"""
def evalRPN(arr):
        stk = []
        ops = {'+', '*', '/', '-'}
        for i, val in enumerate(arr):
            if val in ops:
                n1, n2 = stk.pop(), stk.pop()
                stk.append(str(eval(n2 + val + n1)))
            else:
                stk.append(val)
        return int(float(stk[-1]))


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to evalRPN
    print(evalRPN([]))
