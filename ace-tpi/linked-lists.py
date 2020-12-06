class Node:
    def __init__(self, data):
        self.data = data
        self.next_element = None

class LinkedList:
    def __init__(self):
        self.head_node = None

    def get_head(self):
        return self.head_node

    def is_empty(self):
        if(self.head_node is None):  # Check whether the head is None
            return True
        else:
            return False

    def insert_at_head(self, dt):
        temp_node = Node(dt)
        temp_node.next_element = self.head_node
        self.head_node = temp_node
        return self.head_node

    # Inserts a value at the end of the list
    def insert_at_tail(self, value):
        # Creating a new node
        new_node = Node(value)

        # Check if the list is empty, if it is simply point head to new node
        if self.get_head() is None:
            self.head_node = new_node
            return

        # if list not empty, traverse the list to the last node
        temp = self.get_head()

        while temp.next_element is not None:
            temp = temp.next_element

        # Set the nextElement of the previous node to new node
        temp.next_element = new_node
        return

    def print_list(self):
        if(self.is_empty()):
            print("List is Empty")
            return False
        temp = self.head_node
        while temp.next_element is not None:
            print(temp.data, end=" -> ")
            temp = temp.next_element
        print(temp.data, "-> None")
        return True

    def delete_at_head(self):
        # Get Head and firstElement of List
        first_element = self.get_head()
        # If List is not empty then link head to the
        # nextElement of firstElement.
        if (first_element is not None):
            self.head_node = first_element.next_element
            first_element.next_element = None
        return

    def length(self):
        # start from the first element
        curr = self.get_head()
        length = 0

        # Traverse the list and count the number of nodes
        while curr is not None:
            length += 1
            curr = curr.next_element
        return length

    def search(self, dt):
        if self.is_empty():
            print("List is Empty")
            return None
        temp = self.head_node
        while(temp is not None):
            if(temp.data is dt):
                return temp
            temp = temp.next_element

        print(dt, " is not in List!")
        return None


def insert_at_tail(lst: LinkedList, value: int):
    if lst.is_empty():
        lst.head_node = Node(value)
    else:
        node = lst.get_head()
        while node.next_element is not None:
            node = node.next_element

        new_node = Node(value)
        node.next_element = new_node


def search(lst: LinkedList, value):
    if not lst: return False

    node = lst.get_head()
    while node:
        if node.data == value: return True
        node = node.next_element
    return False


def delete(lst: LinkedList, value):
    if not lst: return False
    node = lst.get_head()

    prev = None
    while node:
        if node.data == value:
            if prev:
                prev.next_element = node.next_element
            else:
                lst.head_node = node.next_element
            return True
        prev = node
        node = node.next_element
    return False


def length(lst):
    len_ = 0
    node = lst.get_head()
    while node:
        len_ += 1
        node = node.next_element
    return len_


def reverse(lst):
    if not lst or not lst.get_head(): return lst

    prev = None
    node = lst.get_head()
    while node:
        node.next_element, prev, node = prev, node, node.next_element
    lst.head_node = prev


def detect_loop(lst: LinkedList):
    if not lst: return False
    slow, fast = lst.get_head(), lst.get_head()
    while slow and fast:
        if slow == fast:
            return True

        slow = slow.next_element
        fast = fast.next_element
        if fast:
            fast = fast.next_element
    return False


def find_mid(lst: LinkedList):
    if not lst or not lst.get_head(): return None

    len_, mid = length(lst), 0
    if len_ % 2 == 1:
        mid = (len_//2) + 1
    else:
        mid = len_//2

    node = lst.get_head()
    for i in range(1, mid+1):
        if i == mid:
            return node
        else:
            node = node.next_element


def remove_duplicates(lst: LinkedList):
    if not lst or not lst.get_head(): return lst

    node, prev, vals = lst.get_head(), None, set()
    while node:
        if node.data in vals:
            prev.next_element = node.next_element
        else:
            vals.add(node.data)
        prev = node
        node = node.next_element
    return lst
