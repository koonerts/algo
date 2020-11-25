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


def reverse_sub_list(head: Node, p: int, q: int):
    """
    Given the head of a LinkedList and two positions ‘p’ and ‘q’, reverse the LinkedList from position ‘p’ to ‘q’.
    """
    dist = abs(p - q) + 1
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
    node, prev, sublist_tail, sublist_tail_prev = head, None, head, head
    k_cntr = k
    is_head_set = False

    while node:
        node.next, prev, node = prev, node, node.next

        k_cntr -= 1
        if k_cntr == 0 or not node:
            if not is_head_set:
                head = prev
                is_head_set = True

            if sublist_tail_prev != sublist_tail:
                sublist_tail_prev.next = prev

            sublist_tail_prev = sublist_tail
            sublist_tail = node
            prev = None
            k_cntr = k

    return head


def reverse_alternate_k_elements(head: Node, k: int) -> Node:
    """
    Given the head of a LinkedList and a number ‘k’, reverse every alternating ‘k’ sized sub-list starting from the head.
    If, in the end, you are left with a sub-list with less than ‘k’ elements, reverse it too.

    Ex:
    Input: 1->2->3->4->5->6->7->8->None, k = 2
    Output: 2->1->3->4->6->5->7->8->None
    """
    node, prev, sublist_tail, non_reverse_tail = head, None, head, None
    k_cntr, should_reverse, is_head_set = k, True, False

    while node:
        if should_reverse:
            node.next, prev, node = prev, node, node.next
            k_cntr -= 1

            if k_cntr == 0 or not node:
                if not is_head_set:
                    head = prev
                    is_head_set = True

                if non_reverse_tail:
                    non_reverse_tail.next = prev

                if sublist_tail:
                    sublist_tail.next = node

                prev = None
        else:
            node = node.next
            k_cntr -= 1
            if k_cntr > 0:
                non_reverse_tail = node
            else:
                sublist_tail = node

        if k_cntr == 0:
            should_reverse = not should_reverse
            k_cntr = k

    return head


def rotate(head: Node, k: int):
    """
    Given the head of a Singly LinkedList and a number ‘k’, rotate the LinkedList to the right by ‘k’ nodes.

    Ex:
    Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None, k = 3
    Output: 4 -> 5 -> 6 -> 1 -> 2 -> 3 -> None
    """
    node = head
    len = 1

    while True:
        if not node.next:
            node.next = head
            break
        else:
            len += 1
            node = node.next

    k %= len
    i = 0
    node, prev_node = head, None

    while i < len - k:
        prev_node = node
        node = node.next
        i += 1

    head = node
    prev_node.next = None
    return head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    # head.next.next.next.next.next = Node(6)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = rotate(head, 8)
    print("Nodes of rotated LinkedList are: ", end='')
    result.print_list()


main()
