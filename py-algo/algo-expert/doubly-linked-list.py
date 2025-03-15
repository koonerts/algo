# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        if not self.head:
            self.head = node
            self.tail = node
        else:
            temp = self.head
            new_head = self.remove(node) or node
            self.head = new_head
            self.head.next = temp
            self.head.prev = None
            temp.prev = self.head

    def setTail(self, node):
        if not self.head:
            self.setHead(node)
        else:
            temp = self.tail
            self.tail = self.remove(node) or node
            self.tail.prev = temp
            self.tail.next = None

    def insertBefore(self, node, nodeToInsert):
        if node == self.head:
            self.setHead(nodeToInsert)
        else:
            nodeToInsert = self.remove(nodeToInsert) or nodeToInsert
            nodeToInsert.prev = node.prev
            nodeToInsert.next = node
            node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        if node == self.tail:
            self.setTail(nodeToInsert)
        else:
            nodeToInsert = self.remove(nodeToInsert) or nodeToInsert
            nodeToInsert.next = node.next
            nodeToInsert.prev = node
            node.next = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        iter_node = self.head
        for _ in range(position - 1):
            iter_node = iter_node.next
        self.insertBefore(iter_node, nodeToInsert)

    def removeNodesWithValue(self, value):
        iter_node = self.head
        while iter_node and iter_node.value != value:
            iter_node = iter_node.next
        if iter_node and iter_node.value == value:
            return self.remove(iter_node)

    def remove(self, node):
        iter_node = self.head
        while iter_node and iter_node != node:
            iter_node = iter_node.next

        if not iter_node:
            return None
        else:
            if iter_node.prev:
                iter_node.prev.next = iter_node.next
            if iter_node.next:
                iter_node.next.prev = iter_node.prev

            iter_node.prev = None
            iter_node.next = None
            return iter_node

    def containsNodeWithValue(self, value):
        iter_node = self.head
        while iter_node and iter_node.value != value:
            iter_node = iter_node.next
        return iter_node and iter_node.value == value
