class Node(object):
    def __init__(self,val = None):
        self.value = val
        self.next = None

class Queue(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0

    def enqueue(self,val):
        node = Node(val)
        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            self.tail = self.tail.next
        self.num_elements += 1
        return

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

    def dequeue(self):
        to_be_returned = self.head.value
        self.head = self.head.next
        self.num_elements -= 1
        return to_be_returned


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