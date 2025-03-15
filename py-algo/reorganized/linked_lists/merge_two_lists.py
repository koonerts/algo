"""
Merge Two Sorted Lists

Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

Example:
    Input: l1 = [1,2,4], l2 = [1,3,4]
    Output: [1,1,2,3,4,4]
    
Time Complexity: O(n + m) where n and m are the lengths of the lists
Space Complexity: O(1) as we only modify pointers
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def __init__(self, val=0, next=None) -> None:
    """
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

Args:
    l1 (Optional[ListNode]): Head of first sorted linked list
l2 (Optional[ListNode]): Head of second sorted linked list
    
Returns:
    Optional[ListNode]: Head of merged sorted linked list
    
Time Complexity: O(n + m) where n and m are the lengths of the lists
Space Complexity: O(1) as we only modify pointers
"""
    val = val
    next = next




# Example usage
if __name__ == "__main__":
    # Create two sorted linked lists:
    # 1->2->4
    l1 = ListNode(1, ListNode(2, ListNode(4)))
    # 1->3->4
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    
    # Merge them
    result = mergeTwoLists(l1, l2)
    
    # Print the merged list
    while result:
        print(result.val, end=" ")
        result = result.next
    # Output: 1 1 2 3 4 4
