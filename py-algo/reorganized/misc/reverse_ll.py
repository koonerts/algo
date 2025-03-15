"""
Reverse_ll

"""


def reverse_ll(head: Node):
    prev = None
    while head is not None:
        next_ = head.next
        head.next = prev
        prev = head
        head = next_
    return prev


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to reverse_ll
    print(reverse_ll([]))
