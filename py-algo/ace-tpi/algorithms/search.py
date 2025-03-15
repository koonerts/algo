from collections import Counter
import math


def linear_search(lst, key):
    if len(lst) <= 0:  # Sanity check
        return -1

    for i in range(len(lst)):
        if lst[i] == key:
            return i  # If found return index
    return -1  # Return -1 otherwise


def binary_search(lst, left, right, key):
    while left <= right:
        mid = left + (right - left) // 2

        # Check if key is present at mid
        if lst[mid] == key:
            return mid
        # If key is greater, ignore left half
        elif lst[mid] < key:
            left = mid + 1
        # If key is smaller, ignore right half
        else:
            right = mid - 1

    # If we reach here, then the element was not present
    return -1


def pivoted_binary_search(lst: list[int], n: int, key: int):
    """
    Function to search key in a list
    :param lst: A list of integers
    :param n: The size of the list
    :param key: A key to be searched in the list
    """
    if n == 0:
        return -1

    l, r = 0, n - 1
    while l <= r:
        mid = (l + r) // 2

        if lst[mid] == key:
            return mid
        else:
            # left sorted
            if lst[l] <= lst[mid]:
                if lst[l] <= key < lst[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # right sorted
            else:
                if lst[mid] < key <= lst[r]:
                    l = mid + 1
                else:
                    r = mid - 1
    return -1


def find_max_prod(lst):
    max_num = max(lst)
    next_max = float("-inf")
    for num in lst:
        if num < max_num:
            next_max = max(next_max, num)

    return next_max, max_num


def find_duplicates(lst):
    num_freq = Counter(lst)
    result = []
    for num in num_freq:
        if num_freq[num] > 1:
            result.append(num)
    return result


class ArrayReader:
    def __init__(self, arr):
        self.arr = arr

    def get(self, index):
        if index >= len(self.arr):
            return math.inf
        return self.arr[index]


def search_in_infinite_array(reader, key):
    i, right = 0, 1
    while reader.get(2**i) < key:
        i += 1
        right = 2**i

    left = 0
    while left <= right:
        mid = (left + right) // 2
        val = reader.get(mid)
        if val == key:
            return mid
        elif val < key:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def search_next_letter(letters, key):
    if key < letters[0] or key >= letters[len(letters) - 1]:
        return letters[0]

    l, r = 0, len(letters) - 1
    while l <= r:
        mid = (l + r) // 2
        if letters[mid] == key:
            return letters[mid + 1]
        elif letters[mid] < key:
            l = mid + 1
        else:
            r = mid - 1
    return letters[l % len(letters)]


def main():
    print(search_next_letter(["a", "c", "f", "h"], "f"))
    print(search_next_letter(["a", "c", "f", "h"], "b"))
    print(search_next_letter(["a", "c", "f", "h"], "m"))


main()
