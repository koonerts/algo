"""
Valid Subsequence

"""
def isValidSubsequence(array, seq):
        seq_idx = 0
        for num in array:
            if seq_idx >= len(seq): return True

            if num == seq[seq_idx]:
                seq_idx += 1
        return False


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to isValidSubsequence
    print(isValidSubsequence([]))
