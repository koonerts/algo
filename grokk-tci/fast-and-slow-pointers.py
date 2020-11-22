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
    vals = {num: 1}
    while True:
        newVal = 0
        for n in map(int, str(num)):
            newVal += n**2

        if newVal == 1:
            return True
        elif vals.get(newVal):
            return False
        else:
            vals[newVal] = 1
            num = newVal


print(find_happy_number(23))