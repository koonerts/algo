"""
One

"""


def plusOne(digits: list[int]) -> list[int]:
    carry_over = 1
    for i in range(len(digits) - 1, -1, -1):
        val = digits[i] + 1 + carry_over
        carry_over = val // 10
        if carry_over > 0:
            digits[i] = 0
        else:
            digits[i] = val

    if carry_over > 0:
        digits.insert(0, 1)
    return digits


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to plusOne
    print(plusOne([]))
