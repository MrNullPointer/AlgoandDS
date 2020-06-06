class Stack(object):
    def __init__(self):
        self.items = list()
    def size(self):
        return len(self.items)
    def push(self,val):
        self.items.append(val)
    def pop(self):
        if self.size() == 0:
            return None
        return self.items.pop()

class Queue(object):
    def __init__(self):
        self.instorage = Stack()
        self.outstorage = Stack()

    def size(self):
        return self.instorage.size() + self.outstorage.size()

    def enqueue(self,val):
        self.instorage.push(val)

    def dequeue(self):
        if self.outstorage.size() == 0:
            while self.instorage.size() != 0:
                self.outstorage.push(self.instorage.pop())
        return self.outstorage.pop()


# Setup
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Test size
print("Pass" if (q.size() == 3) else "Fail")

# Test dequeue
print("Pass" if (q.dequeue() == 1) else "Fail")

# Test enqueue
q.enqueue(4)
print("Pass" if (q.dequeue() == 2) else "Fail")
print("Pass" if (q.dequeue() == 3) else "Fail")
print("Pass" if (q.dequeue() == 4) else "Fail")
q.enqueue(5)
print("Pass" if (q.size() == 1) else "Fail")