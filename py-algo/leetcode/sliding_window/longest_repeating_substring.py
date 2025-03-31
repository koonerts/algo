def longest_repeating_character_replacement(s: str, k: int) -> int:
    """
    Find the length of the longest substring in s, where all characters are identical, after replacing, at
    most, k characters with any other lowercase English character.

    Args:
        s (str): The input string.
        k (int): The maximum number of characters that can be replaced.

    Returns:
        int: The length of the longest substring with all identical characters.
    """
    if not s:
        return 0

    char_count: dict[str, int] = {}
    max_length = 0
    max_count = 0
    left = 0

    for right in range(len(s)):
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        max_count = max(max_count, char_count[s[right]])

        if (right - left + 1) - max_count > k:
            char_count[s[left]] -= 1
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length
