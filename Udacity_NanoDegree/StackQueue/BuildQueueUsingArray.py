'''
Step 1: Init
Define a class named Queue and add the __init__ method
Initialize the arr attribute with an array containing 10 elements, like this: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Initialize the next_index attribute
Initialize the front_index attribute
Initialize the queue_size attribute

Step 2: Enqueue
Take a value as input and assign this value to the next free slot in the array
Increment queue_size
Increment next_index (this is where you'll need to use the modulo operator %)
If the front index is -1 (because the queue was empty), it should set the front index to 0

Step 3:
Add a size method that returns the current size of the queue
Add an is_empty method that returns True if the queue is empty and False otherwise
Add a front method that returns the value for the front element (whatever item is located at the front_index position)...
     ...If the queue is empty, the front method should return None.

Step 4:
If the queue is empty, reset the front_index and next_index and then simply return None. Otherwise...
Get the value from the front of the queue and store this in a local variable (to return later)
Shift the head over so that it refers to the next index
Update the queue_size attribute
Return the value that was dequeued

Step 5:
Define an old_arr variable and assign the the current (full) array so that we have a copy of it
Create a new (larger) array and assign it to arr.
Iterate over the values in the old array and copy them to the new array. Remember that you'll need two for loops for this.
Then, in the enqueue method:

Add a conditional to check if the queue is full; if it is, call _handle_queue_capacity_full
'''

class Queue:
    def __init__(self,size_queue = 10):
        self.arr = [0 for _ in range(size_queue)]
        self.next_index = 0
        self.front_index = -1
        self.queue_size = 0
        return

    def enqueue(self,value):

        # Queue check
        if self.queue_size == len(self.arr):
            self._handle_queue_capacity_full()

        self.arr[self.next_index] = value
        self.queue_size += 1
        self.next_index = (self.next_index + 1) % (len(self.arr))
        if self.front_index == -1:
            self.front_index = 0
        return

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
            return

        value = self.arr[self.front_index]
       # self.next_index -= 1
        self.queue_size -= 1
        self.front_index = (self.front_index + 1) % len(self.arr)
        return value

    def _handle_queue_capacity_full(self):
        old_arr = self.arr
        self.arr = [0 for _ in range(2 * len(self.arr))]
        index = 0
        for i in range(self.front_index,len(old_arr)):
            self.arr[index] = old_arr[i]
            index += 1

        for index in range(0,self.front_index):
            self.arr[index] = old_arr[index]
            index += 1

        self.next_index = index
        self.front_index = 0
        return

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