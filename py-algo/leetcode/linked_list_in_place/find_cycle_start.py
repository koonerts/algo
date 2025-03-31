"""
Find_cycle_start

Given the head of a Singly LinkedList that contains a cycle,
    write a function to find the starting node of the cycle.
"""


def find_cycle_start(head: Node) -> Node:
    """
    Given the head of a Singly LinkedList that contains a cycle,
    write a function to find the starting node of the cycle.
    """
    slow, fast = head, head
    cycle_len = 0
    while True:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            slow = slow.next
            cycle_len += 1
            while slow != fast:
                slow = slow.next
                cycle_len += 1
            break

    start, ahead = head, head
    while cycle_len > 0:
        ahead = ahead.next
        cycle_len -= 1

    while ahead != start:
        ahead = ahead.next
        start = start.next

    return start


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to find_cycle_start
    print(find_cycle_start([]))
