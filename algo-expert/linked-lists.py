
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def create_ll_from_map(m) -> LinkedList:
    head = None
    pass


def removeKthNodeFromEnd(head: LinkedList, k):
    k_ahead = head
    for _ in range(k):
        k_ahead = k_ahead.next

    node, prev = head, None
    while k_ahead:
        prev = node
        node = node.next
        k_ahead = k_ahead.next

    if prev:
        prev.next = node.next
    else:
        head = node.next
        node = None
    return head


head = LinkedList(0)
head.next = LinkedList(1)
head.next.next = LinkedList(2)
head.next.next.next = LinkedList(3)
head.next.next.next.next = LinkedList(4)
head.next.next.next.next.next = LinkedList(5)
head.next.next.next.next.next.next = LinkedList(6)
head.next.next.next.next.next.next.next = LinkedList(7)
head.next.next.next.next.next.next.next.next = LinkedList(8)
head.next.next.next.next.next.next.next.next.next = LinkedList(9)

result = removeKthNodeFromEnd(head, 10)
print(repr(result))
