"""
Has_cycle

Given the head of a Singly LinkedList, write a function to determine if the LinkedList has a cycle in it or not.
"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def has_cycle(head: Node) -> bool:
    """
    Given the head of a Singly LinkedList, write a function to determine if the LinkedList has a cycle in it or not.
    """
    if not head:
        return False

    slow, fast = head, head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return True  # found the cycle
    return False


# Example usage
if __name__ == "__main__":
    # Create a linked list with a cycle
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = head.next  # create a cycle
    print(has_cycle(head))  # Output: True

    # Create a linked list without a cycle
    head2 = Node(1)
    head2.next = Node(2)
    head2.next.next = Node(3)
    print(has_cycle(head2))  # Output: False
