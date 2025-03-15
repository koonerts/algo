from heapq import *


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

    def print_list(self):
        temp = self
        while temp is not None:
            if temp.next:
                print(temp.value, end="->")
            else:
                print(temp.value, end="")
            temp = temp.next
        print()


def create_ll_from_map(nmap) -> LinkedList:
    head = None
    node_map = {}
    nmap = nmap.get("linkedList", nmap)
    for n in nmap["nodes"]:
        node = LinkedList(n["value"])
        node_map[n["id"]] = node
        if n["id"] == nmap["head"]:
            head = node

    for n in nmap["nodes"]:
        if n["next"] is not None:
            node = node_map[n["id"]]
            node.next = node_map[n["next"]]
    return head


def removeKthNodeFromEnd(head: LinkedList, k):
    k_ahead = head
    for _ in range(k):
        k_ahead = k_ahead.next

    node, prev = head, None
    while k_ahead:
        prev = node
        node = node.next
        k_ahead = k_ahead.next

    if prev:
        prev.next = node.next
    else:
        node = head
        while node:
            node.value = node.next.value
            if not node.next.next.next:
                node.next = None
                node = None
                break
            node = node.next


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


def shiftLinkedList(head, k):
    ll_len = 0
    node = head
    while node:
        ll_len += 1
        node = node.next

    k %= ll_len
    if k == 0:
        return head

    node, prev = head, None
    for _ in range(ll_len - k):
        prev = node
        node = node.next
    new_head = node
    prev.next = None

    while node:
        if not node.next:
            node.next = head
            break
        node = node.next
    return new_head


def rearrangeLinkedList(head, k):
    low_head, low_tail, k_head, k_tail, hi_head, hi_tail = (
        None,
        None,
        None,
        None,
        None,
        None,
    )
    node = head
    while node:
        if node.value < k:
            if not low_head:
                low_head, low_tail = node, node
            else:
                low_tail.next = node
                low_tail = low_tail.next
        elif node.value > k:
            if not hi_head:
                hi_head, hi_tail = node, node
            else:
                hi_tail.next = node
                hi_tail = hi_tail.next
        else:
            if not k_head:
                k_head, k_tail = node, node
            else:
                k_tail.next = node
                k_tail = k_tail.next
        node = node.next

    new_head = low_head or k_head or hi_head
    if low_tail:
        if k_head:
            low_tail.next = k_head
        else:
            low_tail.next = hi_head
    if k_tail:
        k_tail.next = hi_head
    if hi_tail:
        hi_tail.next = None
    return new_head


def linkedListPalindrome(head):
    if not head or not head.next:
        return True

    len = 0
    node = head
    while node:
        len += 1
        node = node.next

    mid = len // 2
    node, prev = head, None
    for _ in range(mid):
        temp = node.next
        node.next = prev
        prev = node
        node = temp

    p1, p2 = prev, node
    if len % 2 == 1:
        p2 = p2.next
    p1.print_list()
    p2.print_list()

    while p1 or p2:
        if (not p1 and p2) or (p1 and not p2) or (p1.value != p2.value):
            return False
        p1 = p1.next
        p2 = p2.next
    return True


nmap = {
    "linkedList": {
        "head": "6",
        "nodes": [
            {"id": "6", "next": "5", "value": 6},
            {"id": "5", "next": "4", "value": 5},
            {"id": "4", "next": "3", "value": 4},
            {"id": "3", "next": "4-2", "value": 3},
            {"id": "4-2", "next": "5-2", "value": 4},
            {"id": "5-2", "next": "6-2", "value": 5},
            {"id": "6-2", "next": None, "value": 6},
        ],
    }
}

root = create_ll_from_map(nmap)
root.print_list()
res = linkedListPalindrome(root)
print(res)
