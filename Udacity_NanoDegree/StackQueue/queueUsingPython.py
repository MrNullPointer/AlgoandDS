class Queue:
    def __init__(self):
        self.arr = list()

    # TODO: Initialize the Queue

    def size(self):
        return len(self.arr)

    # TODO: Check the size of the Queue

    def enqueue(self, item):
        self.arr.append(item)

    # TODO: Enter item into Queue

    def dequeue(self):
        return self.arr.pop(0)
# TODO: Remove item from the Queue

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