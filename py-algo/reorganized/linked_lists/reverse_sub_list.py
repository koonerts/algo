"""
Reverse_sub_list

Given the head of a LinkedList and two positions ‘p’ and ‘q’, reverse the LinkedList from position ‘p’ to ‘q’.
"""
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



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to reverse_sub_list
    print(reverse_sub_list([]))
