"""
Linked List Cycle

Given head, the head of a linked list, determine if the linked list has a cycle in it. There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.

Example:
    Input: head = [3,2,0,-4], pos = 1 (pos denotes the index of the node that tail's next pointer is connected to)
    Output: true (there is a cycle in the linked list)
    
Time Complexity: O(n) where n is the number of nodes in the list
Space Complexity: O(1) as we only use two pointers regardless of list size
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head: Optional[ListNode]) -> bool:
    """
    Given head, the head of a linked list, determine if the linked list has a cycle in it.
    
    Uses Floyd's Cycle-Finding Algorithm (Tortoise and Hare approach) to detect cycles
    with O(1) space complexity.
    
    Args:
        head (Optional[ListNode]): Head of the linked list
        
    Returns:
        bool: True if the linked list has a cycle, False otherwise
        
    Time Complexity: O(n) where n is the number of nodes in the list
    Space Complexity: O(1) as we only use two pointers regardless of list size
    """
    if not head or not head.next:
        return False
        
    # Initialize slow and fast pointers
    slow, fast = head, head
    
    # Move slow pointer by 1 and fast pointer by 2
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        # If there's a cycle, the fast pointer will eventually catch up to the slow pointer
        if slow == fast:
            return True
            
    # If we reach the end of the list, there's no cycle
    return False


# Example usage
if __name__ == "__main__":
    # Create a linked list with a cycle: 3->2->0->-4->2...
    head = ListNode(3)
    node1 = ListNode(2)
    node2 = ListNode(0)
    node3 = ListNode(-4)
    head.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node1  # Creates a cycle
    
    print(hasCycle(head))  # Output: True
    
    # Create a linked list without a cycle: 1->2->3->None
    head2 = ListNode(1, ListNode(2, ListNode(3)))
    print(hasCycle(head2))  # Output: False