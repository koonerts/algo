"""
Repeated DNA Sequences

Problem: Find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

A DNA sequence is represented as a string consisting of the letters A, C, G, and T,
which represent the nucleotides adenine, cytosine, guanine, and thymine.

Example:
Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC", "CCCCCAAAAA"]
"""


def findRepeatedDnaSequences(s: str) -> list[str]:
    """
    Find all 10-letter-long sequences that occur more than once in the DNA string.

    This implementation uses a rolling hash technique (similar to Rabin-Karp algorithm)
    for efficiently identifying repeated sequences without having to compare every
    character in each subsequence.

    Args:
        s: A string representing a DNA sequence with characters A, C, G, and T

    Returns:
        A list of strings, each representing a 10-letter sequence that appears multiple times
    """
    # Map each nucleotide to an integer for hash computation
    to_int = {"A": 0, "C": 1, "G": 2, "T": 3}
    encoded_sequence = [to_int[c] for c in s]

    k, n = 10, len(s)  # k is the length of sequences we're looking for

    # Edge case: input string is shorter than k
    if n <= k:
        return []

    a = 4  # Base value (number of possible characters in DNA)
    h = 0  # Initial hash value
    seen_hashes, output = set(), set()  # Track seen hashes and repeated sequences
    a_k = 1  # Will hold a^k for the rolling hash calculation

    # Calculate initial hash for the first window and a^k
    for i in range(k):
        h = h * a + encoded_sequence[i]
        a_k *= a  # Calculate a^k (4^10)

    # Add the initial hash to our set
    seen_hashes.add(h)

    # Use rolling hash to check all other windows
    for start in range(1, n - k + 1):
        # Update hash: remove contribution of the leftmost character and add contribution of new rightmost character
        # Formula: h = h * a - leftmost * a^k + rightmost
        h = h * a - encoded_sequence[start - 1] * a_k + encoded_sequence[start + k - 1]

        # If we've seen this hash before, we found a repeat
        if h in seen_hashes:
            output.add(s[start : start + k])
        else:
            seen_hashes.add(h)

    return list(output)


# Driver code
def main():
    """Test the function with various examples."""
    test_cases = [
        "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",  # Multiple repeats
        "AAAAAAAAAAAAA",  # Overlapping repeats
        "ACGTACGTACGTACGTACGTACGTACGTACGT",  # Periodic pattern
        "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG",  # All same character
        "GTACGTACGTACGCCCCCCCCGGGGG",  # No repeats
    ]

    for i, s in enumerate(test_cases):
        print(f'{i+1}.\tInput: "{s}"')
        print(f"\n\tOutput: {findRepeatedDnaSequences(s)}")
        print("-" * 100)


if __name__ == "__main__":
    main()


"""
Time Complexity Analysis:
- O(n) where n is the length of the input string
- We process each character exactly once with constant time operations

Space Complexity Analysis:
- O(n) for storing the hash values and output sequences
- In the worst case, we could have O(n-k) unique sequences

Note on Hash Collisions:
- The rolling hash method can have collisions (different sequences producing the same hash)
- For DNA sequences with only 4 characters and a fixed length of 10, the chance of collision is very low
- For production systems, additional verification or a more robust hash algorithm might be needed
"""
