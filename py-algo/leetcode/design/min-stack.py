class MinStack:
    def __init__(self):
        self.min_stk = []
        self.stk = []

    # @param x, an integer
    def push(self, x):
        self.stk.append(x)
        if not self.min_stk or x < self.min_stk[-1]:
            self.min_stk.append(x)

    # @return nothing
    def pop(self):
        if self.stk:
            val = self.stk.pop()
            if val == self.min_stk[-1]:
                self.min_stk.pop()
            return val

    # @return an integer
    def top(self):
        return self.stk[-1] if self.stk else -1

    # @return an integer
    def getMin(self):
        return self.min_stk[-1] if self.min_stk else -1