from heapq import *


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

    def print_list(self):
        temp = self
        while temp is not None:
            if temp.next: print(temp.value, end="->")
            else: print(temp.value, end="")
            temp = temp.next
        print()


def create_ll_from_map(nmap) -> LinkedList:
    head = None
    node_map = {}
    for n in nmap['nodes']:
        node = LinkedList(n['value'])
        node_map[n['id']] = node
        if n['id'] == nmap['head']:
            head = node

    for n in nmap['nodes']:
        if n['next'] is not None:
            node = node_map[n['id']]
            node.next = node_map[n['next']]
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

nmap = {
    "head": "0",
    "nodes": [
        {"id": "0", "next": "1", "value": 0},
        {"id": "1", "next": "2", "value": 1},
        {"id": "2", "next": "3", "value": 2},
        {"id": "3", "next": "4", "value": 3},
        {"id": "4", "next": "5", "value": 4},
        {"id": "5", "next": None, "value": 5}
    ]
}


root = create_ll_from_map(nmap)
res = shiftLinkedList(root, -8)
res.print_list()
