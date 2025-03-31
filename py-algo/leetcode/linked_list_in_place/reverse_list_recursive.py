"""
List Recursive

"""
def reverseListRecursive(head: ListNode) -> ListNode:
def reverse(curr: ListNode, prev: ListNode = None) -> ListNode:
            if not curr:
                return prev

            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            return reverse(curr, prev)
        return reverse(head)


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to reverseListRecursive
    print(reverseListRecursive([]))
