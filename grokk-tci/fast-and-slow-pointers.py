class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end='')
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

    def reverse_ll(head):
        prev = None
        while head is not None:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev

    reverse_second_half = reverse_ll(slow)
    copy_reverse_second_half = reverse_second_half

    is_palindrome = True
    while head and reverse_second_half:
        if head.value != reverse_second_half.value and reverse_second_half.value is not None:
            is_palindrome = False
            break

        head = head.next
        reverse_second_half = reverse_second_half.next

    reverse_ll(copy_reverse_second_half)
    return is_palindrome


def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)

    print("Is palindrome: " + str(is_palindromic_linked_listv2(head)))

    head.next.next.next.next.next = Node(2)
    print("Is palindrome: " + str(is_palindromic_linked_listv2(head)))


main()