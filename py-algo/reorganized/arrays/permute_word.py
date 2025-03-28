def permute_word(word):
    result = []
    n = len(word)
    used = [False] * n
    current_permutation = []

    def backtrack():
        # Base case: a full permutation is formed
        if len(current_permutation) == n:
            result.append("".join(current_permutation))
            return

        # Explore adding an unused character
        for i in range(n):
            if not used[i]:
                # Choose
                used[i] = True
                current_permutation.append(word[i])

                # Explore
                backtrack()

                # Unchoose (backtrack)
                current_permutation.pop()
                used[i] = False

    backtrack()  # Start the backtracking process
    return result
