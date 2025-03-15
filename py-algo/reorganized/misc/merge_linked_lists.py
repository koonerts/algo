"""
Linked Lists

"""


def mergeLinkedLists(headOne, headTwo):
    n1, n2 = headOne, headTwo
    head: LinkedList
    if n1.value <= n2.value:
        head = n1
        n1 = n1.next
    else:
        head = n2
        n2 = n2.next

    prev = head
    while n1 or n2:
        if n1 and n2:
            if n1.value <= n2.value:
                prev.next = n1
                prev = n1
                n1 = n1.next
            else:
                prev.next = n2
                prev = n2
                n2 = n2.next
        elif n1:
            prev.next = n1
            prev = n1
            n1 = n1.next
        else:
            prev.next = n2
            prev = n2
            n2 = n2.next
    return head


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to mergeLinkedLists
    print(mergeLinkedLists([]))
