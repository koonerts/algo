"""
Is_palindromic_linked_list

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


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to is_palindromic_linked_list
    print(is_palindromic_linked_list([]))
