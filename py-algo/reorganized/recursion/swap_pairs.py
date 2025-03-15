"""
Pairs

"""
def swapPairs(head: ListNode) -> ListNode:
        if not head.next: return head
def swap_rec(node, prev, prev_sublist_tail, k):
            if not node:
                if prev_sublist_tail and prev and (prev_sublist_tail != prev):
                    prev_sublist_tail.next = prev
                if prev:
                    prev.next = None
            else:
                if k == 1:
                    temp = node.next
                    node.next = prev
                    if prev_sublist_tail:
                        prev_sublist_tail.next = node
                    swap_rec(temp, prev, prev, (k+1) % 2)
                else:
                    swap_rec(node.next, node, prev_sublist_tail, (k+1) % 2)

        new_head = head.next
        swap_rec(head, prev=None, prev_sublist_tail=head, k=0)
        return new_head


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to swapPairs
    print(swapPairs([]))
