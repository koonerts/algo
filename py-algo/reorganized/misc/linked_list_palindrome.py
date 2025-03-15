"""
List Palindrome

"""
def linkedListPalindrome(head):
    if not head or not head.next: return True

    len = 0
    node = head
    while node:
        len += 1
        node = node.next

    mid = len//2
    node, prev = head, None
    for _ in range(mid):
        temp = node.next
        node.next = prev
        prev = node
        node = temp

    p1, p2 = prev, node
    if len % 2 == 1:
        p2 = p2.next
    p1.print_list()
    p2.print_list()

    while p1 or p2:
        if (not p1 and p2) or (p1 and not p2) or (p1.value != p2.value):
            return False
        p1 = p1.next
        p2 = p2.next
    return True



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to linkedListPalindrome
    print(linkedListPalindrome([]))
