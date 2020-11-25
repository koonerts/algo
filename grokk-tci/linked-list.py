
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


def reverse(head: Node) -> Node:
    prev = None
    while head:
        head.next, prev, head = prev, head, head.next
    return prev


def reverse_sub_list(head: Node, p: int, q:int):
    """
    Given the head of a LinkedList and two positions ‘p’ and ‘q’, reverse the LinkedList from position ‘p’ to ‘q’.
    """
    dist = abs(p-q) + 1
    node, prev_p_node, p_node = head, None, None

    while not p_node:
        if node.value == p:
            p_node = node
        else:
            prev_p_node = node
            node = node.next

    node = p_node
    prev = None
    while dist > 0:
        node.next, prev, node = prev, node, node.next
        dist -= 1

        if dist == 0:
            if prev_p_node:
                prev_p_node.next = prev
            if node:
                p_node.next = node

    return head


def reverse_every_k_elements(head: Node, k: int):
    """
    Given the head of a LinkedList and a number ‘k’, reverse every ‘k’ sized sub-list starting from the head.
    If, in the end, you are left with a sub-list with less than ‘k’ elements, reverse it too.
    """
    node, prev, prev_sublist_end = head, None, None
    k_cntr = k
    is_head_set = False

    while node:
        node.next, prev, node = prev, node, node.next

        k_cntr -= 1
        if (k_cntr == 0 or not node) and not is_head_set:
            head = prev
            is_head_set = True

        if k_cntr == 0 and node:
            prev.next = node
            k_cntr = k
    return head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_every_k_elements(head, 3)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()