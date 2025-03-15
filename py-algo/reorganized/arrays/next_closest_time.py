"""
Closest Time

"""


def nextClosestTime(time: str) -> str:
    valid_digits = [int(c) for c in time if c != ":"]
    valid_digits.sort()

    new_time = ""
    for i in range(len(time) - 1, -1, -1):
        if time[i] == ":":
            new_time = ":" + new_time
            continue

        val = next((d for d in valid_digits if d > int(time[i])), valid_digits[0])
        new_time = str(val) + new_time
        if val != valid_digits[0]:
            return time[:i] + new_time


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to nextClosestTime
    print(nextClosestTime([]))
