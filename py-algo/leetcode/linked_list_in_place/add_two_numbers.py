"""
Two Numbers

https://leetcode.com/problems/add-two-numbers/
"""


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    """https://leetcode.com/problems/add-two-numbers/"""

    carry_over = 0
    head, prev_digit_node = None, None
    while l1 or l2:
        l1_val = 0 if not l1 else l1.val
        l2_val = 0 if not l2 else l2.val
        digit_sum = l1_val + l2_val + carry_over

        digit_node = ListNode(digit_sum % 10)
        if prev_digit_node:
            prev_digit_node.next = digit_node
        else:
            head = digit_node

        prev_digit_node = digit_node
        carry_over = digit_sum // 10

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

        if not l1 and not l2 and carry_over == 1:
            digit_node = ListNode(1)
            prev_digit_node.next = digit_node

    return head


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to addTwoNumbers
    print(addTwoNumbers([]))
