"""
Search_next_letter

Given an array of lowercase letters sorted in ascending order,
    find the smallest letter in the given array greater than a given ‘key’.

    Assume the given array is a circular list, which means that the last letter is assumed to be
    connected with the first letter. This also means that the smallest letter in the given array is
    greater than the last letter of the array and is also the first letter of the array.

    Write a function to return the next letter of the given ‘key’.

    Example 1:
    Input: ['a', 'c', 'f', 'h'], key = 'f'
    Output: 'h'
    Explanation: The smallest letter greater than 'f' is 'h' in the given array.

    Example 2:
    Input: ['a', 'c', 'f', 'h'], key = 'b'
    Output: 'c'
    Explanation: The smallest letter greater than 'b' is 'c'.

    Example 3:
    Input: ['a', 'c', 'f', 'h'], key = 'm'
    Output: 'a'
    Explanation: As the array is assumed to be circular, the smallest letter greater than 'm' is 'a'.

    Example 4:
    Input: ['a', 'c', 'f', 'h'], key = 'h'
    Output: 'a'
    Explanation: As the array is assumed to be circular, the smallest letter greater than 'h' is 'a'.
"""


def search_next_letter(letters: list[str], key: str) -> str:
    """
    Given an array of lowercase letters sorted in ascending order,
    find the smallest letter in the given array greater than a given ‘key’.

    Assume the given array is a circular list, which means that the last letter is assumed to be
    connected with the first letter. This also means that the smallest letter in the given array is
    greater than the last letter of the array and is also the first letter of the array.

    Write a function to return the next letter of the given ‘key’.

    Example 1:
    Input: ['a', 'c', 'f', 'h'], key = 'f'
    Output: 'h'
    Explanation: The smallest letter greater than 'f' is 'h' in the given array.

    Example 2:
    Input: ['a', 'c', 'f', 'h'], key = 'b'
    Output: 'c'
    Explanation: The smallest letter greater than 'b' is 'c'.

    Example 3:
    Input: ['a', 'c', 'f', 'h'], key = 'm'
    Output: 'a'
    Explanation: As the array is assumed to be circular, the smallest letter greater than 'm' is 'a'.

    Example 4:
    Input: ['a', 'c', 'f', 'h'], key = 'h'
    Output: 'a'
    Explanation: As the array is assumed to be circular, the smallest letter greater than 'h' is 'a'.
    """
    if letters[-1] <= key or letters[0] > key:
        return letters[0]

    start, end = 0, len(letters) - 1

    while start <= end:
        mid = int((start + end) / 2)
        if letters[mid] == key:
            if mid + 1 <= len(letters) - 1:
                return letters[mid + 1]
            else:
                return letters[0]
        elif letters[mid] < key:
            start = mid + 1
        else:
            end = mid - 1

    return letters[0] if start > len(letters) - 1 else letters[start]


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to search_next_letter
    print(search_next_letter([]))
