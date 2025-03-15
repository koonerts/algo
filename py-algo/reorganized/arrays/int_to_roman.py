"""
To Roman

"""


def intToRoman(num: int) -> str:
    digits = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I",
    }


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to intToRoman
    print(intToRoman([]))
