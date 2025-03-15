"""
Has_cycle

Given the head of a Singly LinkedList, write a function to determine if the LinkedList has a cycle in it or not.

class Node:
def __init__(self, value, next=None):
    self.value = value
    self.next = next
"""
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


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to has_cycle
    print(has_cycle([]))
