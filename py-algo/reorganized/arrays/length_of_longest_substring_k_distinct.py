"""
Of Longest Substring K Distinct

"""
def lengthOfLongestSubstringKDistinct(s: str, k: int) -> int:
        if k == 0: return 0

        freq, lo = {}, 0
        max_len = 0
        for hi, v in enumerate(s):
            if len(freq) < k or v in freq:
                freq[v] = freq.get(v, 0) + 1
            else:
                while len(freq) >= k:
                    if freq[s[lo]] == 1:
                        del freq[s[lo]]
                    else:
                        freq[s[lo]] -= 1
                    lo += 1
                freq[v] = freq.get(v, 0) + 1
            max_len = max(max_len, hi-lo+1)
        return max_len


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to lengthOfLongestSubstringKDistinct
    print(lengthOfLongestSubstringKDistinct([]))
