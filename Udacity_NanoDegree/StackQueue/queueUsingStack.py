# In this exercise we are going to create a queue with just stacks.

class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size() == 0:
            return None
        else:
            return self.items.pop()


class Queue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def size(self):
        return self.stack1.size() + self.stack2.size()

    # Code here

    def enqueue(self, item):
        self.stack1.push(item)

    # Code here

    def dequeue(self):
        if not self.stack2.items:
            while self.stack1.items:
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()

# Setup
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Test size
print ("Pass" if (q.size() == 3) else "Fail")

# Test dequeue
print ("Pass" if (q.dequeue() == 1) else "Fail")

# Test enqueue
q.enqueue(4)
print ("Pass" if (q.dequeue() == 2) else "Fail")
print ("Pass" if (q.dequeue() == 3) else "Fail")
print ("Pass" if (q.dequeue() == 4) else "Fail")
q.enqueue(5)
print ("Pass" if (q.size() == 1) else "Fail") 