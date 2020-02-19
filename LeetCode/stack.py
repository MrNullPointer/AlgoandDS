class stack(object):
    def __init__(self):
        self.stack = []
    def push(self,x):
        self.stack.append(x)
    def pop(self):
        if len(self.stack) > 0:
            self.stack.pop()
        else:
            return None
    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack) - 1]
        else:
            return None
    def __str__(self):
        return str(self.stack)


my_stack = stack()
my_stack.pop()
my_stack.push(2)
my_stack.push(4)
print(my_stack.peek())
print(my_stack)