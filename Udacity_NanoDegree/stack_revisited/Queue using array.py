'''
enqueue - adds data to the back of the queue
dequeue - removes data from the front of the queue
front - returns the element at the front of the queue
size - returns the number of elements present in the queue
is_empty - returns True if there are no elements in the queue, and False otherwise
_handle_full_capacity - increases the capacity of the array, for cases in which the queue would otherwise overflow
'''

class Queue(object):
    def __init__(self,size = 1):
        self.arr = [0 for _ in range(size)]
        self.next_index = 0
        self.queue_size = 0
        self.front_index = -1

    def enqueue(self,val):
        if self.front_index == -1:
            self.front_index = 0

        if self.size() == len(self.arr):
            self._handle_queue_full_capacity()
        self.arr[self.next_index] = val
        self.next_index = (self.next_index + 1) % len(self.arr)
        self.queue_size += 1

    def size(self):
        return self.queue_size

    def is_empty(self):
        return self.queue_size == 0

    def front(self):
        if self.front_index == -1:
            return None
        return self.arr[self.front_index]

    def dequeue(self):
        if self.is_empty():
            self.front_index = -1
            self.next_index = 0
            return None
        temp = self.arr[self.front_index]
        self.front_index = (self.front_index + 1) % len(self.arr)
        self.queue_size -= 1
        return temp

    def _handle_queue_full_capacity(self):
        old_queue = None
        if self.front_index == 0:
            old_queue = self.arr
        else:
            for elem in range(0, self.front_index):
                old_queue[elem] = self.arr[elem]
            for val in range(self.front_index,len(self.arr)):
                old_queue[val] = self.arr[val]

        self.arr = [1 for _ in range(2 * len(self.arr))]
        index = 0
        for value in range(len(old_queue)):
            self.arr[value] = old_queue[value]
            index += 1

        self.front_index = 0
        self.next_index = index



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