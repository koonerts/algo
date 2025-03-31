"""
Palindrome

"""


def isPalindrome(head: ListNode) -> bool:
    head_copy = head
    reversed_head = self.reverseList(head_copy)
    while head or reversed_head:
        if (head and not reversed_head) or (reversed_head and not head):
            return False
        if head.val != reversed_head.val:
            return False
        head = head.next
        reversed_head = reversed_head.next
    return True


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to isPalindrome
    print(isPalindrome([]))
