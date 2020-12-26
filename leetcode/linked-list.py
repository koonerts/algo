from heapq import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # def __lt__(self, other):
    #     other_val = other.val if other else float('inf')
    #     return self.val < other_val

    def print_list(self):
        vals = ''
        node = self
        while node:
            if node:
                vals += str(node.val)
            if node.next:
                vals += '->'
            node = node.next

        print(vals)

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
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

            if l1: l1 = l1.next
            if l2: l2 = l2.next

            if not l1 and not l2 and carry_over == 1:
                digit_node = ListNode(1)
                prev_digit_node.next = digit_node

        return head

    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        prev = node
        curr = node.next
        while curr:
            prev.val = curr.val

            if not curr.next:
                prev.next = None
                break

            prev = curr
            curr = curr.next

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        prev, node, ahead_node = None, head, head
        for _ in range(n):
            ahead_node = ahead_node.next

        while ahead_node:
            ahead_node = ahead_node.next
            prev = node
            node = node.next

        if prev and node:
            prev.next = node.next

        if head == node:
            head = head.next

        return head

    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        while head:
            head.next, prev, head = prev, head, head.next
        return prev

    def reverseListRecursive(self, head: ListNode) -> ListNode:
        def reverse(curr: ListNode, prev: ListNode = None) -> ListNode:
            if not curr:
                return prev

            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            return reverse(curr, prev)
        return reverse(head)

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2
        elif not l2: return l1

        head: ListNode
        if l1.val <= l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next

        node = head
        while l1 or l2:
            if not l1:
                node.next = l2
                l2 = None
            elif not l2:
                node.next = l1
                l1 = None
            else:
                if l1.val <= l2.val:
                    node.next = l1
                    l1 = l1.next
                    node = node.next
                else:
                    node.next = l2
                    l2 = l2.next
                    node = node.next
        return head

    def isPalindrome(self, head: ListNode) -> bool:
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

    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        if not lists: return None

        min_heap = []
        for i in range(len(lists)):
            head = lists[i]
            if head: heappush(min_heap, (head.val, head))

        head, prev = None, None
        while min_heap:
            val, node = heappop(min_heap)
            if node.next:
                heappush(min_heap, (node.val, node.next))

            if not head:
                head = node
            else:
                prev.next = node

            prev = node
        return head


node1 = ListNode(1, ListNode(4, ListNode(5)))
node2 = ListNode(1, ListNode(3, ListNode(4)))
node3 = ListNode(2, ListNode(6))

val = Solution().mergeKLists([node1, node2, node3])
val.print_list()
