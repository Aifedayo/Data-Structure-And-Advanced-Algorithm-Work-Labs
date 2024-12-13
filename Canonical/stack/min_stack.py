class MinStack:
    def __init__(self):
        self.main = []
        self.min = []

    def push(self, value):
        if len(self.min) == 0:
            self.min.append(value)
        elif value < self.min[-1]:
            self.min.append(value)
        else:
            self.min.append(self.min[-1])
        self.main.append(value)

    def pop(self):
        self.min.pop()
        return self.main.pop()


min_stack = MinStack()
min_stack.push(10)
min_stack.push(15)
min_stack.push(5)
print(min_stack.main)
print(min_stack.min)