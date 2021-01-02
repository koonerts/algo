

def find_peak(lst):
    """
    Finds a peak element
    :param lst: List of integers
    :return: Returns a peak element in a given list
    """

    def find_peak_recursive(low, high, lst):
        # Finding the middle index
        middle = low + (high - low) // 2

        # If there are neighbours
        if (middle == len(lst) - 1 or lst[middle + 1] <= lst[middle]) and (middle == 0 or lst[middle - 1] <= lst[middle]):
            return middle

        # If left neighbour is greater, then peak element is in the left half
        elif (lst[middle - 1] > lst[middle]) and middle > 0:
            return find_peak_recursive(low, (middle - 1), lst)

        # If right neighbour is greater, then peak element is in the right half
        else:
            return find_peak_recursive((middle + 1), high, lst)

    return lst[find_peak_recursive(0, len(lst) - 1, lst)]


def max_sub_list_of_size_k(lst, k):
    """
    Finds a maximum sum of a sub-list of given window size k
    :param lst: List of integers
    :param k: Window size of the list
    :return: Returns the maximum sum of a sub-list of given window size k
    """
    left = 0
    max_sum = float('-inf')
    curr_sum = 0
    for i, v in enumerate(lst):
        if i < k:
            curr_sum += v
        else:
            if max_sum == float('-inf'):
                max_sum = max(max_sum, curr_sum)

            curr_sum += v
            curr_sum -= lst[left]
            left += 1
            max_sum = max(max_sum, curr_sum)
    return max_sum


def minimum_steps(lst):
    """
    Function which calculates the minimum steps to collect coins from the list
    :param lst: List of coins stack
    :return: Returns minimum steps to collect coins from the list, otherwise 0
    """
    pass


def find_floor(lst, low, high, x):
    """
    Modified binary search function to find the floor of given number x
    :param lst: List of integers
    :param low: Starting index of the list
    :param high: Ending index of the list
    :return: Returns the floor of an integer x if exists, otherwise -1
    """
    if lst[0] >= x: return -1
    elif lst[-1] < x: return high

    while low <= high:
        mid = (low+high)//2

        if lst[mid] == x:
            if mid == 0: return -1
            else: return lst[mid - 1]
        elif lst[mid] < x:
            if mid+1 < len(lst) and lst[mid+1] < x:
                low = mid + 1
            else:
                return lst[mid]
        else:
            high = mid - 1
    return -1

def find_ceiling(lst, low, high, x):
    """
    Modified binary search function to find the floor of given number x
    :param lst: List of integers
    :param low: Starting index of the list
    :param high: Ending index of the list
    :return: Returns the ceiling of an integer x if exists, otherwise -1
    """
    if lst[-1] <= x: return -1
    elif lst[0] > x: return lst[0]

    while low <= high:
        mid = (low+high)//2

        if lst[mid] == x:
            if mid == len(lst) - 1: return -1
            else: return lst[mid + 1]
        elif lst[mid] < x:
            low = mid + 1
        else:
            if mid-1 >= 0 and lst[mid-1] <= x:
                return lst[mid]
            else:
                high = mid - 1
    return -1


def find_closest(lst, target):
    """
    Finds the closest number to the target in the list
    :param lst: Sorted list of integers
    :param target: Left sided index of the list
    :return: Closest element from the list to the target
    """
    l, r = 0, len(lst) - 1
    min_diff_ele, min_diff = float('inf'), float('inf')
    while l <= r:
        pass


print(max_sub_list_of_size_k([-1,-2,-3,-4,-5,-6], 2))