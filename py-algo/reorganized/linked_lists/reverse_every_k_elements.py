"""
Reverse_every_k_elements

"""
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



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to reverse_every_k_elements
    print(reverse_every_k_elements([]))
