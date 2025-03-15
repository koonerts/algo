"""
Find_happy_number

Any number will be called a happy number if, after repeatedly replacing it with a number equal to
    the sum of the square of all of its digits, leads us to number ‘1’.
    All other (not-happy) numbers will never reach ‘1’.
    Instead, they will be stuck in a cycle of numbers which does not include ‘1’.
"""
def find_happy_number(num: int) -> bool:
    """
    Any number will be called a happy number if, after repeatedly replacing it with a number equal to
    the sum of the square of all of its digits, leads us to number ‘1’.
    All other (not-happy) numbers will never reach ‘1’.
    Instead, they will be stuck in a cycle of numbers which does not include ‘1’.
    """
    slow, fast = num, num
def find_squared_digit_sum(val) -> int:
        new_val = 0
        for n in map(int, str(val)):
            new_val += n**2
        return new_val

    while True:
        slow = find_squared_digit_sum(slow)
        fast = find_squared_digit_sum(find_squared_digit_sum(fast))

        if slow == 1 or fast == 1:
            return True
        elif slow == fast:
            return False



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to find_happy_number
    print(find_happy_number([]))
