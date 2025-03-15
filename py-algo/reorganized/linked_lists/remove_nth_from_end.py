"""
Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example:
    Input: head = [1,2,3,4,5], n = 2
    Output: [1,2,3,5] (the 2nd node from the end, which is 4, is removed)
    
Time Complexity: O(n) where n is the length of the list
Space Complexity: O(1) as we only use a constant amount of extra space
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def __init__(self, val=0, next=None) -> None:
    """
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Args:
    head (Optional[ListNode]): Head of the linked list
n (int): Position from the end to remove (1-indexed)
    
Returns:
    Optional[ListNode]: Head of the modified linked list
    
Time Complexity: O(n) where n is the length of the list
Space Complexity: O(1) as we only use a constant amount of extra space
"""
    val = val
    next = next




# Example usage
if __name__ == "__main__":
    # Create a linked list: 1->2->3->4->5
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    
    # Remove the 2nd node from the end
    result = removeNthFromEnd(head, 2)
    
    # Print the result
    while result:
        print(result.val, end=" ")
        result = result.next
    # Output: 1 2 3 5
