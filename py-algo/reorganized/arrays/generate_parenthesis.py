def generate_combinations(n):
    """Problem: Generate Parentheses
    Statement

    For a given number, n, generate all combinations of balanced parentheses.

    Constraints:
        1 <= n <= 10
    """
    combos=[]
    def backtrack(curr_combo: list[str], lcount: int, rcount:int) -> None:
        if len(curr_combo) == 2*n:
            combos.append("".join(curr_combo))
            return

        if lcount < n:
            curr_combo.append('(')
            backtrack(curr_combo, lcount+1, rcount)
            curr_combo.pop()

        if rcount < n and lcount > rcount:
            curr_combo.append(')')
            backtrack(curr_combo, lcount, rcount+1)
            curr_combo.pop()

    backtrack([], 0, 0)
    return combos
