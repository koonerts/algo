class MyStack:
    def __init__(self):
        self.stack_list = []

    def is_empty(self):
        return len(self.stack_list) == 0

    def top(self):
        if self.is_empty():
            return None
        return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack_list.pop()


class MyQueue:
    def __init__(self):
        self.queue_list = []

    def is_empty(self):
        return self.size() == 0

    def front(self):
        if self.is_empty():
            return None
        return self.queue_list[0]

    def back(self):
        if self.is_empty():
            return None
        return self.queue_list[-1]

    def size(self):
        return len(self.queue_list)

    def enqueue(self, value):
        self.queue_list.append(value)

    def dequeue(self):
        if self.is_empty():
            return None
        front = self.front()
        self.queue_list.remove(self.front())
        return front


def reverseK(queue: MyQueue, k: int):
    if not queue or queue.is_empty() or queue.size() < k or k < 0: return None

    new_queue = MyQueue()
    first_k = []
    for _ in range(k):
        if queue.is_empty():
            break

        first_k.append(queue.dequeue())

    while len(first_k) > 0:
        new_queue.enqueue(first_k.pop())

    while not queue.is_empty():
        new_queue.enqueue(queue.dequeue())
    return new_queue


class NewQueue:
    def __init__(self):
        self.main_stack = MyStack()
        self.secondary_stack = MyStack()

    def enqueue(self, value):
        self.main_stack.push(value)
        return True

    def dequeue(self):
        if self.secondary_stack.is_empty():
            while not self.main_stack.is_empty():
                self.secondary_stack.push(self.main_stack.pop())

        return self.secondary_stack.pop()


def evaluate_post_fix(exp: str) -> int:
    exp = exp.replace(' ', '')
    stack = MyStack()

    for c in exp:
        if c.isnumeric():
            stack.push(c)
        else:
            y = stack.pop()
            x = stack.pop()
            val = str(eval(f'{x}{c}{y}'))
            stack.push(val)
    return int(float(stack.top()))


def next_greater_element(lst: list[int]):
    """
    TODO: Come back to -> https://www.educative.io/module/lesson/data-structures-in-python/JEqRg24VJxl
    """
    ret_list = []
    stack = MyStack()


class MinStack:
    """
    TODO: Come back to -> https://www.educative.io/module/lesson/data-structures-in-python/qV5y32RxMRp
    """

    # Constructor
    def __init__(self):
        self.main_stack = MyStack()
        self.min_stack = MyStack()

    # Removes and return value from newStack
    def pop(self):
        # Write your code here
        return -1

    # Pushes values into newStack
    def push(self, value):
        # Write your code here
        return False

    # Returns minimum value from newStack in O(1) Time
    def min(self):
        # Write your code here
        pass

    # Write any helper functions here