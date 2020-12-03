class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    """https://leetcode.com/problems/add-two-numbers/"""

    # def reverse_linked_list(head: ListNode) -> ListNode:
    #     prev, node = None, head
    #     while node:
    #         node.next, prev, node = prev, node, node.next
    #     return prev

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

        if l1: l1 = l1.next
        if l2: l2 = l2.next

        if not l1 and not l2 and carry_over == 1:
            digit_node = ListNode(1)
            prev_digit_node.next = digit_node

    return head