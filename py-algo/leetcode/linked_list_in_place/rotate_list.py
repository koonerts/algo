"""
Rotate_list

"""


def rotate_list(head: Node, n: int):
    if not head or n == 0:
        return head

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
        return new_head


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to rotate_list
    print(rotate_list([]))
