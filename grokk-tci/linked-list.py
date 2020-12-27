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


def reverse_every_k_elements(head: Node, k: int) -> Node:
    k_cntr, sublist_cntr = 1, 0
    sublist_tail, sublist_tail_prev, node, prev, new_head = head, head, head, None, None

    while node:
        temp = node.next
        temp = node.next
        node.next = prev
        prev = node
        node = temp

        if k_cntr % k == 0 or not node:
            if not new_head:
                new_head = prev
            else:
                sublist_tail_prev.next = prev
                sublist_tail_prev = sublist_tail
            sublist_tail = node
            prev = None
        k_cntr += 1
    return new_head


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


def rotate_list(head: Node, n: int):
    if not head or n == 0: return head

    len = 0
    node = head
    while node:
        len += 1
        node = node.next

    if abs(n) % len == 0:
        return head
    else:
        iter_rng = 0
        if n > 0:
            iter_rng = len - (n % len)
        else:
            iter_rng = abs(n) % len

        node, prev = head, None
        for _ in range(iter_rng):
            node, prev = node.next, node
        prev.next = None

        new_head = node
        while node.next:
            node = node.next
        node.next = head
        return new_head\


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = rotate_list(head, -2)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()

main()
