"""
Reverse Linked List

Reverse a singly linked list.

Example:
    Input: 1->2->3->4->5->NULL
    Output: 5->4->3->2->1->NULL

Time Complexity: O(n) where n is the number of nodes in the list
Space Complexity: O(1) as we only use a constant amount of extra space
"""


class ListNode:
def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


def __init__(self, val=0, next=None) -> None:
    """
    Reverse a singly linked list.

    Args:
        head (Optional[ListNode]): Head of the linked list

    Returns:
        Optional[ListNode]: New head of the reversed linked list

    Time Complexity: O(n) where n is the number of nodes in the list
    Space Complexity: O(1) as we only use a constant amount of extra space
    """
    val = val
    next = next


# Example usage
if __name__ == "__main__":
    # Create a linked list: 1->2->3->4->5
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    # Reverse it
    new_head = reverse(head)
    # Print the reversed list
    while new_head:
        print(new_head.val, end=" ")
        new_head = new_head.next
    # Output: 5 4 3 2 1
