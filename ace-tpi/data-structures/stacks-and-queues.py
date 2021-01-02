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
    ret_list = [-1 for i in lst]
    stack = MyStack()

    for i in range(len(lst) - 1, -1, -1):
        while not stack.is_empty() and stack.top() <= lst[i]:
            stack.pop()

        if not stack.is_empty():
            ret_list[i] = stack.top()
        stack.push(lst[i])
    print(ret_list)
    return ret_list


class MinStack:
    # Constructor
    def __init__(self):
        self.min_stack = MyStack()
        self.main_stack = MyStack()
        return

        # Removes and returns value from min_stack
    def pop(self):
        self.min_stack.pop()
        return self.main_stack.pop()

        # Pushes values into min_stack
    def push(self, value):
        self.main_stack.push(value)
        if(self.min_stack.is_empty() or self.min_stack.top() > value):
            self.min_stack.push(value)
        else:
            self.min_stack.push(self.min_stack.top())


        # Returns minimum value from newStack in O(1) Time
    def min(self):
        if not self.min_stack.is_empty():
            return self.min_stack.top()


stack = MinStack()
stack.push(3)
stack.push(4)
stack.push(2)
stack.push(4)
stack.pop()

print(stack.main_stack.stack_list)
print("minimum value: " + str(stack.min()))

stack.pop()
print(stack.main_stack.stack_list)
print("minimum value: " + str(stack.min()))