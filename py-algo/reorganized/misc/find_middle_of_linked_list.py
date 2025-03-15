"""
Find_middle_of_linked_list

Input: 1 -> 2 -> 3 -> 4 -> 5 -> null
    Output: 3

    Example 2:
    Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null
    Output: 4

    Example 3:
    Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> null
    Output: 4
"""


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


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to find_middle_of_linked_list
    print(find_middle_of_linked_list([]))
