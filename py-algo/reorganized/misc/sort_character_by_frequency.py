"""
Sort_character_by_frequency

Given a string, sort it based on the decreasing frequency of its characters.

    Example 1:
    Input: "Programming"
    Output: "rrggmmPiano"
    Explanation: 'r', 'g', and 'm' appeared twice, so they need to appear before any other character.

    Example 2:
    Input: "abcbab"
    Output: "bbbaac"
    Explanation: 'b' appeared three times, 'a' appeared twice, and 'c' appeared only once.
"""
def sort_character_by_frequency(str):
    """
    Given a string, sort it based on the decreasing frequency of its characters.

    Example 1:
    Input: "Programming"
    Output: "rrggmmPiano"
    Explanation: 'r', 'g', and 'm' appeared twice, so they need to appear before any other character.

    Example 2:
    Input: "abcbab"
    Output: "bbbaac"
    Explanation: 'b' appeared three times, 'a' appeared twice, and 'c' appeared only once.
    """
    freq_map = {}

    for c in str:
        freq_map[c] = freq_map.get(c, 0) + 1

    max_heap = []
    for c, freq in freq_map.items():
        heappush(max_heap, (-freq, c))

    ret_list = []
    while max_heap:
        freq, c = heappop(max_heap)
        ret_list += c*-freq

    return ''.join(ret_list)



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to sort_character_by_frequency
    print(sort_character_by_frequency([]))
