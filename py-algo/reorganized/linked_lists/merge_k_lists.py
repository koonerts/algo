"""
K Lists

"""
def mergeKLists(lists: list[ListNode]) -> ListNode:
        if not lists: return None

        min_heap = []
        for i in range(len(lists)):
            head = lists[i]
            if head: heappush(min_heap, (head.val, head))

        head, prev = None, None
        while min_heap:
            val, node = heappop(min_heap)
            if node.next:
                heappush(min_heap, (node.val, node.next))

            if not head:
                head = node
            else:
                prev.next = node

            prev = node
        return head



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to mergeKLists
    print(mergeKLists([]))
