'''
Step 1: Create a queue class
A head attribute to keep track of the first node in the linked list
A tail attribute to keep track of the last node in the linked list
A num_elements attribute to keep track of how many items are in the stack

Step 2: Enqueue method
If the queue is empty, then both the head and tail should refer to the new node (because when there's only one node,...
 ...this node is both the head and the tail)
Otherwise (if the queue has items), add the new node to the tail (i.e., to the end of the queue)
Be sure to shift the tail reference so that it refers to the new node (because it is the new tail)

Step 3: size and is_empty method
Add a size method that returns the current size of the stack
Add an is_empty method that returns True if the stack is empty and False otherwise

Step 4: Dequeue method:
If the queue is empty, it should simply return None. Otherwise...
Get the value from the front of the queue (i.e., the head of the linked list)
Shift the head over so that it refers to the next node
Update the num_elements attribute
Return the value that was dequeued
'''

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0

    def enqueue(self,value):
        new_node = Node(value)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
        self.num_elements += 1
        return

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.head == None

    def dequeue(self):
        if self.head is None:
            return None
        value = self.head.value
        self.head = self.head.next
        self.num_elements -= 1
        return value

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