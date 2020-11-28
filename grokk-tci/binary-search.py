
def binary_search(arr: list[int], key: int) -> int:
    """
    Given a sorted array of numbers, find if a given number ‘key’ is present in the array.
    Though we know that the array is sorted, we don’t know if it’s sorted in ascending or descending order.
    You should assume that the array can have duplicates.
    Write a function to return the index of the ‘key’ if it is present in the array, otherwise return -1.

    Example 1:
    Input: [4, 6, 10], key = 10
    Output: 2

    Example 2:
    Input: [1, 2, 3, 4, 5, 6, 7], key = 5
    Output: 4

    Example 3:
    Input: [10, 6, 4], key = 10
    Output: 0

    Example 4:
    Input: [10, 6, 4], key = 4
    Output: 2
    """
    if not arr: return -1

    start, end = 0, len(arr)-1
    is_ascending = True if len(arr) > 1 and arr[0] < arr[1] else False

    while start <= end:
        mid = int((start+end) / 2)

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            if is_ascending:
                start = mid+1
            else:
                end = mid-1
        else:
            if is_ascending:
                end = mid-1
            else:
                start = mid+1

    return False


def search_ceiling_of_a_number(arr: list[int], key: int) -> int:
    """
    Given an array of numbers sorted in an ascending order, find the ceiling of a given number ‘key’.
    The ceiling of the ‘key’ will be the smallest element in the given array greater than or equal to the ‘key’.
    Write a function to return the index of the ceiling of the ‘key’. If there isn’t any ceiling return -1.

    Example 1:
    Input: [4, 6, 10], key = 6
    Output: 1
    Explanation: The smallest number greater than or equal to '6' is '6' having index '1'.

    Example 2:
    Input: [1, 3, 8, 10, 15], key = 12
    Output: 4
    Explanation: The smallest number greater than or equal to '12' is '15' having index '4'.

    Example 3:
    Input: [4, 6, 10], key = 17
    Output: -1
    Explanation: There is no number greater than or equal to '17' in the given array.

    Example 4:
    Input: [4, 6, 10], key = -1
    Output: 0
    Explanation: The smallest number greater than or equal to '-1' is '4' having index '0'.
    """
    if not arr or arr[-1] < key:
        return -1

    start, end = 0, len(arr)-1
    while start <= end:
        mid = int((start+end) / 2)

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            start = mid+1
        else:
            end = mid-1

    return start


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

    start, end = 0, len(letters)-1

    while start <= end:
        mid = int((start+end) / 2)
        if letters[mid] == key:
            if mid+1 <= len(letters)-1:
                return letters[mid+1]
            else:
                return letters[0]
        elif letters[mid] < key:
            start = mid+1
        else:
            end = mid-1

    return letters[0] if start > len(letters)-1 else letters[start]


def find_range(arr: list[int], key: int) -> list[int]:
    """
    Given an array of numbers sorted in ascending order, find the range of a given number ‘key’.
    The range of the ‘key’ will be the first and last position of the ‘key’ in the array.
    Write a function to return the range of the ‘key’. If the ‘key’ is not present return [-1, -1].

    Example 1:
    Input: [4, 6, 6, 6, 9], key = 6
    Output: [1, 3]

    Example 2:
    Input: [1, 3, 8, 10, 15], key = 10
    Output: [3, 3]

    Example 3:
    Input: [1, 3, 8, 10, 15], key = 12
    Output: [-1, -1]
    """
    if not arr: return [- 1, -1]

    start, end = 0, len(arr)-1

    while start <= end:
        mid = (start+end)//2
        if arr[mid] == key:
            break
        elif arr[mid] < key:
            start = mid+1
        else:
            end = mid-1

    if start > end: return [-1, -1]


def find_range2(arr, key):
    result = [- 1, -1]
    result[0] = binary_search2(arr, key, False)
    if result[0] != -1:  # no need to search, if 'key' is not present in the input array
        result[1] = binary_search2(arr, key, True)
    return result


def binary_search2(arr, key, findMaxIndex):
    keyIndex = -1
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if key < arr[mid]:
            end = mid - 1
        elif key > arr[mid]:
            start = mid + 1
        else:  # key == arr[mid]
            keyIndex = mid
            if findMaxIndex:
                start = mid + 1  # search ahead to find the last index of 'key'
            else:
                end = mid - 1  # search behind to find the first index of 'key'

    return keyIndex


def search_min_diff_element(arr: list[int], key:int) -> int:
    """
    Given an array of numbers sorted in ascending order, find the element in the array
    that has the minimum difference with the given ‘key’.

    Example 1:
    Input: [4, 6, 10], key = 7
    Output: 6
    Explanation: The difference between the key '7' and '6' is minimum than any other number in the array

    Example 2:
    Input: [4, 6, 10], key = 4
    Output: 4

    Example 3:
    Input: [1, 3, 8, 10, 15], key = 12
    Output: 10

    Example 4:
    Input: [4, 6, 10], key = 17
    Output: 10
    """
    if key <= arr[0]: return arr[0]
    elif key >= arr[len(arr)-1]: return arr[len(arr)-1]

    start, end = 0, len(arr)-1

    while start <= end:
        mid = (start+end)//2

        if arr[mid] == key:
            return key
        elif arr[mid] < key:
            start = mid + 1
        else:
            end = mid - 1

    start_diff = abs(key - arr[start])
    end_diff = abs(key - arr[end])

    if start_diff <= end_diff:
        return arr[start]
    else:
        return arr[end]


def find_index_of_max_in_bitonic_array(arr) -> int:
    """
    Find the maximum value in a given Bitonic array.
    An array is considered bitonic if it is monotonically increasing and then monotonically decreasing.
    Monotonically increasing or decreasing means that for any index i in the array arr[i] != arr[i+1].

    Example 1:
    Input: [1, 3, 8, 12, 4, 2]
    Output: 12
    Explanation: The maximum number in the input bitonic array is '12'.

    Example 2:
    Input: [3, 8, 3, 1]
    Output: 8

    Example 3:
    Input: [1, 3, 8, 12]
    Output: 12

    Example 4:
    Input: [10, 9, 8]
    Output: 10
    """
    if len(arr) <= 2:
        return 0

    start, end = 0, len(arr) - 1

    while start <= end:
        mid = (start+end)//2

        if mid+1 <= len(arr)-1 and arr[mid] < arr[mid+1]:
            start = mid + 1
        elif end-1 >= 0 and arr[mid] < arr[mid-1]:
            end = mid - 1
        else:
            return mid


def search_bitonic_array(arr, key):
    """
    Given a Bitonic array, find if a given ‘key’ is present in it.
    An array is considered bitonic if it is monotonically increasing and then monotonically decreasing.
    Monotonically increasing or decreasing means that for any index i in the array arr[i] != arr[i+1].
    Write a function to return the index of the ‘key’. If the ‘key’ is not present, return -1.

    Example 1:
    Input: [1, 3, 8, 4, 3], key=4
    Output: 3

    Example 2:
    Input: [3, 8, 3, 1], key=8
    Output: 1

    Example 3:
    Input: [1, 3, 8, 12], key=12
    Output: 3

    Example 4:
    Input: [10, 9, 8], key=10
    Output: 0
    """
    def b_search(start, end, is_ascending) -> int:
        while start <= end:
            mid = (start + end)//2
            if arr[mid] == key:
                return mid
            elif arr[mid] < key:
                if is_ascending:
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                if is_ascending:
                    end = mid - 1
                else:
                    start = mid + 1
        return -1

    max_index = find_index_of_max_in_bitonic_array(arr)
    if key == arr[max_index]:
        return max_index
    else:
        i = b_search(0, max_index - 1, True)

        # search descending half
        if i == -1 and key < arr[max_index]:
            i = b_search(max_index+1, len(arr)-1, False)

        return i


def search_rotated_array(arr, key) -> int:
    """
    Given an array of numbers which is sorted in ascending order and is
    also rotated by some arbitrary number, find if a given ‘key’ is present in it.

    Write a function to return the index of the ‘key’ in the rotated array.
    If the ‘key’ is not present, return -1.
    You can assume that the given array does not have any duplicates.

    Example 1:
    Input: [10, 15, 1, 3, 8], key = 15
    Output: 1
    Explanation: '15' is present in the array at index '1'.
    """
    return -1


def main():
    print(search_rotated_array([10, 15, 1, 3, 8], 15))
    print(search_rotated_array([4, 5, 7, 9, 10, -1, 2], 10))


main()
