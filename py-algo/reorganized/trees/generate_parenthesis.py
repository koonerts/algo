"""
Parenthesis

"""
def generateParenthesis(n: int) -> list[str]:
        result = []
        if n <= 0: return result
def add_parenthesis(curr_str, open_cnt, closed_cnt):
            if closed_cnt == n:
                result.append(curr_str)
            else:
                if open_cnt < n:
                    add_parenthesis(curr_str+'(', open_cnt+1, closed_cnt)
                if closed_cnt < open_cnt:
                    add_parenthesis(curr_str+')', open_cnt, closed_cnt+1)

        add_parenthesis('', 0, 0)
        return result


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to generateParenthesis
    print(generateParenthesis([]))
