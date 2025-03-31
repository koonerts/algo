"""
Reverse

"""


def reverse(x: int) -> int:
    reversed_x = 0
    is_neg, x = x < 0, abs(x)

    while x != 0:
        r = x % 10
        reversed_x = reversed_x * 10 + r
        x = x // 10

    if is_neg:
        reversed_x = -reversed_x

    return 0 if not (-(2**31) - 1 <= reversed_x <= 2**31 - 1) else reversed_x


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to reverse
    print(reverse([]))
