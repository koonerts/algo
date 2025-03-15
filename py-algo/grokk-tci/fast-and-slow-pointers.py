class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(str(temp.value) + " ", end="")
            temp = temp.next
        print()


def has_cycle(head: Node) -> bool:
    """
    Given the head of a Singly LinkedList, write a function to determine if the LinkedList has a cycle in it or not.

    class Node:
        def __init__(self, value, next=None):
            self.value = value
            self.next = next
    """
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return True  # found the cycle
    return False


def find_cycle_start(head: Node) -> Node:
    """
    Given the head of a Singly LinkedList that contains a cycle,
    write a function to find the starting node of the cycle.
    """
    slow, fast = head, head
    cycle_len = 0
    while True:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            slow = slow.next
            cycle_len += 1
            while slow != fast:
                slow = slow.next
                cycle_len += 1
            break

    start, ahead = head, head
    while cycle_len > 0:
        ahead = ahead.next
        cycle_len -= 1

    while ahead != start:
        ahead = ahead.next
        start = start.next

    return start


def find_happy_number(num: int) -> bool:
    """
    Any number will be called a happy number if, after repeatedly replacing it with a number equal to
    the sum of the square of all of its digits, leads us to number ‘1’.
    All other (not-happy) numbers will never reach ‘1’.
    Instead, they will be stuck in a cycle of numbers which does not include ‘1’.
    """
    slow, fast = num, num

    def find_squared_digit_sum(val) -> int:
        new_val = 0
        for n in map(int, str(val)):
            new_val += n**2
        return new_val

    while True:
        slow = find_squared_digit_sum(slow)
        fast = find_squared_digit_sum(find_squared_digit_sum(fast))

        if slow == 1 or fast == 1:
            return True
        elif slow == fast:
            return False


def find_middle_of_linked_list(head: Node) -> Node:
    """
    Input: 1 -> 2 -> 3 -> 4 -> 5 -> null
    Output: 3

    Example 2:
    Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null
    Output: 4

    Example 3:
    Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> null
    Output: 4
    """
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def is_palindromic_linked_list(head: Node) -> bool:
    """
    Given the head of a Singly LinkedList, write a method to check if the LinkedList is a palindrome or not.
    Your algorithm should use constant space and the input LinkedList should be in the original form once the algorithm is finished.
    The algorithm should have O(N) time complexity where ‘N’ is the number of nodes in the LinkedList.

    Example 1:
    Input: 2 -> 4 -> 6 -> 4 -> 2 -> null
    Output: true

    Example 2:
    Input: 2 -> 4 -> 6 -> 4 -> 2 -> 2 -> null
    Output: false
    """
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    reverse_second_half = reverse_ll(slow)
    copy_reverse_second_half = reverse_second_half

    is_palindrome = True
    while head and reverse_second_half:
        if (
            head.value != reverse_second_half.value
            and reverse_second_half.value is not None
        ):
            is_palindrome = False
            break

        head = head.next
        reverse_second_half = reverse_second_half.next

    reverse_ll(copy_reverse_second_half)
    return is_palindrome


def reverse_ll(head: Node):
    prev = None
    while head is not None:
        next_ = head.next
        head.next = prev
        prev = head
        head = next_
    return prev


def reorder(head: Node):
    """
    Given the head of a Singly LinkedList, write a method to modify the LinkedList such that the
    nodes from the second half of the LinkedList are inserted alternately to the nodes from the first half in reverse order.
    So if the LinkedList has nodes 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null, your method should return 1 -> 6 -> 2 -> 5 -> 3 -> 4 -> null.
    Your algorithm should not use any extra space and the input LinkedList should be modified in-place.

    Example 1:
    Input: 2 -> 4 -> 6 -> 8 -> 10 -> 12 -> null
    Output: 2 -> 12 -> 4 -> 10 -> 6 -> 8 -> null

    Example 2:
    Input: 2 -> 4 -> 6 -> 8 -> 10 -> null
    Output: 2 -> 10 -> 4 -> 8 -> 6 -> null
    """
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    end_to_mid = reverse_ll(slow)

    cntr = 0
    start = head
    while start.next:
        if cntr % 2 == 0:
            if start:
                next_start = start.next
                start.next = end_to_mid
                start = next_start
        else:
            if start:
                next_end_to_mid = end_to_mid.next
                end_to_mid.next = start
                end_to_mid = next_end_to_mid
            else:
                break
        cntr += 1

    return


def circular_array_loop_exists(arr: list[int]) -> bool:
    """
    We are given an array containing positive and negative numbers. Suppose the array contains a number ‘M’ at a particular index.
    Now, if ‘M’ is positive we will move forward ‘M’ indices and if ‘M’ is negative move backwards ‘M’ indices.
    You should assume that the array is circular which means two things:
        - If, while moving forward, we reach the end of the array, we will jump to the first element to continue the movement.
        - If, while moving backward, we reach the beginning of the array, we will jump to the last element to continue the movement.

    Write a method to determine if the array has a cycle. The cycle should have more than one element and
    should follow one direction which means the cycle should not contain both forward and backward movements.

    Example 1:

    Input: [1, 2, -1, 2, 2]
    Output: true
    Explanation: The array has a cycle among indices: 0 -> 1 -> 3 -> 0

    Example 2:
    Input: [2, 2, -1, 2]
    Output: true
    Explanation: The array has a cycle among indices: 1 -> 3 -> 1

    Example 3:
    Input: [2, 1, -1, -2]
    Output: false
    Explanation: The array does not have any cycle.
    """

    def get_index(curr_index: int, curr_direction: int) -> int:
        new_direction = 1 if arr[curr_index] > 0 else -1
        if new_direction != direction:
            return -1

        new_index = (curr_index + arr[curr_index]) % len(arr)

        if new_index == curr_index:
            return -1
        return new_index

    for i in range(len(arr)):
        slow, fast = i, i
        direction = 1 if arr[i] > 0 else -1

        while True:
            slow = get_index(slow, direction)
            fast = get_index(fast, direction)
            if fast == -1:
                break

            fast = get_index(fast, direction)
            if fast == -1 or slow == -1 or slow == fast:
                break

        if slow == -1 and slow == fast:
            return False
        elif slow == fast:
            return True
    return False


def main():
    print(circular_array_loop_exists([1, 2, -1, 2, 2]))
    print(circular_array_loop_exists([2, 2, -1, 2]))
    print(circular_array_loop_exists([2, 1, -1, -2]))


main()
