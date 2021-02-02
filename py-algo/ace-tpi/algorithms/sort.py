import random


def selection_sort(lst):
    # Traverse through all lst elements
    for i in range(len(lst)):
        # Find the minimum element in unsorted lst
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[min_index] > lst[j]:
                min_index = j

        # Swap the found minimum element with the first element
        lst[i], lst[min_index] = lst[min_index], lst[i]


def bubble_sort(lst):
    # Traverse through all list elements
    for i in range(len(lst)):
        # Last i elements are already in place
        for j in range(0, len(lst) - i - 1):
            # Traverse the list from 0 to size of lst - i - 1
            # Swap if the element found is greater than the next element
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]


def insertion_sort(lst):
    # Traverse through 1 to len(lst)
    for i in range(1, len(lst)):
        key = lst[i]
        # Move elements of lst greater than key, to one position ahead
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key


def merge_sort(lst):
    if len(lst) > 1:
        mid = len(lst) // 2  # Mid of the list
        left = lst[:mid]  # Dividing the list elements into 2 halves
        right = lst[mid:]

        merge_sort(left)  # Sorting the first half
        merge_sort(right)  # Sorting the second half

        # Initializing index variables
        i, j, k = 0, 0, 0

        # Copy data to temp lists left[] and right[]
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1

        # Checking if any element was right
        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1


def quick_sort(lst, left, right):
    """
    Quick sort function
    :param lst: lst of unsorted integers
    :param left: Left index of sub-list
    :param right: right-index of sub-list
    """

    def partition(lst, left, right):
        """
        Partition the list on the basis of pivot
        :param left: Left index of sub-list
        :param right: right-index of sub-list
        """

        def choose_pivot(left, right):
            """
            Function to choose pivot point
            :param left: Left index of sub-list
            :param right: right-index of sub-list
            """

            # Pick 3 random numbers within the range of the list
            i1 = left + random.randint(0, right - left)
            i2 = left + random.randint(0, right - left)
            i3 = left + random.randint(0, right - left)

            # Return their median
            return max(min(i1, i2), min(max(i1, i2), i3))

        pivot_index = choose_pivot(left, right)  # Index of pivot

        lst[right], lst[pivot_index] = lst[pivot_index], lst[right]  # put the pivot at the end

        pivot = lst[right]  # Pivot
        i = left - 1  # All the elements less than or equal to the
        # pivot go before or at i

        for j in range(left, right):
            if lst[j] <= pivot:
                i += 1  # increment the index
                lst[i], lst[j] = lst[j], lst[i]

        lst[i + 1], lst[right] = lst[right], lst[i + 1]  # Putting the pivot back in place
        return i + 1

    if left < right:
        # pi is where the pivot is at
        pi = partition(lst, left, right)

        # Separately sort elements before and after partition
        quick_sort(lst, left, pi - 1)
        quick_sort(lst, pi + 1, right)


def sort_binary_list(lst):
    l, r = 0, len(lst) - 1
    while l < r:
        if lst[l] == 1:
            lst[l], lst[r] = lst[r], lst[l]
            r -= 1
        else:
            l += 1


def dutch_national_flag_sort(lst):
    l, r = 0, len(lst)-1
    while l < r:
        if lst[l] == 0:
            l += 1
        else:
            if lst[r] == 1:
                m = r - 1
                while m > 0 and lst[m] == 1:
                    m -= 1
                lst[m], lst[r] = lst[r], lst[m]
            lst[l], lst[r] = lst[r], lst[l]
            r -= 1


x = [2, 0, 0, 1, 2, 1, 0]
dutch_national_flag_sort(x)
print(x)