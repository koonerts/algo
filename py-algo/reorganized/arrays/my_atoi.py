"""
Atoi

"""
def myAtoi(s: str) -> int:
        if not s: return 0

        start, end = -1, -1
        for i, c in enumerate(s):
            if c in ['+', '-'] or c.isnumeric():
                start = i
                end = i + 1
                while end < len(s) and s[end].isnumeric():
                    end += 1
                break
            elif c.isspace():
                continue
            else:
                return 0

        sign = '+'

        if s[start] == '+':
            start += 1
            if s[start] == '-':
                sign = '-'
                start += 1
        elif s[start] == '-':
            sign = '-'
            start += 1
            if s[start] == '-':
                sign = '-'
                start += 1

        if not s[start:end].isnumeric():
            return 0

        val = int(s[start:end])
        if val > 2 ** 31:
            return 2 ** 31
        elif val < (-2) ** 31:
            return (-2) ** 31
        else:
            return val


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to myAtoi
    print(myAtoi([]))
