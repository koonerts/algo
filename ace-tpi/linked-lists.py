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
        if(self.is_empty()):
            self.head_node = temp_node
            return self.head_node

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

    def length(self):
        # start from the first element
        curr = self.get_head()
        length = 0

        # Traverse the list and count the number of nodes
        while curr is not None:
            length += 1
            curr = curr.next_element
        return length

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

    def delete(self, value):
        deleted = False
        if self.is_empty():  # Check if list is empty -> Return False
            print("List is Empty")
            return deleted
        current_node = self.get_head()  # Get current node
        previous_node = None  # Get previous node
        if current_node.data is value:
            self.delete_at_head()  # Use the previous function
            deleted = True
            return deleted

        # Traversing/Searching for Node to Delete
        while current_node is not None:
            # Node to delete is found
            if value is current_node.data:
                # previous node now points to next node
                previous_node.next_element = current_node.next_element
                current_node.next_element = None
                deleted = True
                break
            previous_node = current_node
            current_node = current_node.next_element

        return deleted

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

    def remove_duplicates(self):
        if self.is_empty():
            return

        # If list only has one node, leave it unchanged
        if self.get_head().next_element is None:
            return

        outer_node = self.get_head()
        while outer_node:
            inner_node = outer_node  # Iterator for the inner loop
            while inner_node:
                if inner_node.next_element:
                    if outer_node.data == inner_node.next_element.data:
                        # Duplicate found, so now removing it
                        new_next_element = inner_node.next_element.next_element
                        inner_node.next_element = new_next_element
                    else:
                        # Otherwise simply iterate ahead
                        inner_node = inner_node.next_element
                else:
                    # Otherwise simply iterate ahead
                    inner_node = inner_node.next_element
            outer_node = outer_node.next_element
        return


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


def union(list1: LinkedList, list2: LinkedList):
    if not list1: return list2
    elif not list2: return list1
    elif not list1 and not list2: return None

    l1_node = list1.get_head()
    while l1_node.next_element:
        l1_node = l1_node.next_element
    l1_node.next_element = list2.get_head()

    list1.remove_duplicates()
    return list1


def intersection(list1: LinkedList, list2: LinkedList):
    if not list1 or not list2 or not list1.get_head() or not list2.get_head():
        return None

    # Write your code here
    list2_set = set()
    list2_node = list2.get_head()
    while list2_node:
        list2_set.add(list2_node.data)
        list2_node = list2_node.next_element

    ret_list, intersection_head, prev = None, None, None
    list1_node = list1.get_head()
    while list1_node:
        if list1_node.data in list2_set:
            if not intersection_head:
                intersection_head = Node(list1_node.data)
                ret_list = LinkedList()
                ret_list.head_node = intersection_head
                prev = intersection_head
            else:
                node = Node(list1_node.data)
                prev.next_element = node
                prev = node

        list1_node = list1_node.next_element

    ret_list.remove_duplicates()
    return ret_list


def find_nth(lst: LinkedList, n: int) -> int:
    if not lst or not lst.get_head(): return -1

    lst_node, n_ahead = lst.get_head(), lst.get_head()
    for _ in range(n):
        if not n_ahead: return -1
        n_ahead = n_ahead.next_element

    while n_ahead:
        n_ahead = n_ahead.next_element
        lst_node = lst_node.next_element
    return lst_node.data


def find_happy_number(num: int):
    def get_squared_sum(number: int) -> int:
        s = 0
        for n in [int(x) for x in str(number)]:
            s += n**2
        return s

    slow_squared_sum, fast_squared_sum = num, num
    while True:
        slow_squared_sum = get_squared_sum(slow_squared_sum)
        fast_squared_sum = get_squared_sum(get_squared_sum(fast_squared_sum))

        if slow_squared_sum == 1 or fast_squared_sum == 1:
            return True
        elif slow_squared_sum == fast_squared_sum:
            return False


def main():
    print(find_happy_number(23))
    print(find_happy_number(12))


main()

