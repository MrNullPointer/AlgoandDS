'''
First Step:
Define a class named Stack and add the __init__ method
Initialize the arr attribute with an array containing 10 elements, like this: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Initialize the next_index attribute
Initialize the num_elements attribute

Step Push:
First, define the _handle_stack_capacity_full method:

Define an old_arr variable and assign it the current (full) array
Create a new (larger) array and assign it to arr.
Iterate over the values in the old array and copy them to the new array.
Then, in the push method:

Add a conditional to check if the array is full; if it is, call the _handle_stack_capacity_full
'''
class Stack:
    def __init__(self,number_of_elements = 10):
        self.arr = [0 for _ in range(number_of_elements)]
        self.next_index = 0
        self.num_elements = 0

    def push(self,value):
        if self.next_index == len(self.arr):
            print("Increasing the size of stack....")
            self._handle_stack_capacity_full()
        self.arr[self.next_index] = value
        self.next_index += 1
        self.num_elements += 1

    def _handle_stack_capacity_full(self):
        old_stack = self.arr
        self.arr = [0 for _ in range(2 * len(old_stack))]

        for index,value in enumerate(old_stack):
            self.arr[index] = value

        return None

    # Add a size method that returns the current size of the stack
    def size(self):
        return self.num_elements

    # Add an is_empty method that returns True if the stack is empty and False otherwise
    def is_empty(self):
        return self.num_elements == 0

    def pop(self):
        if self.is_empty():
            return None
        self.next_index -= 1
        self.num_elements -= 1
        return self.arr[self.next_index]

foo = Stack()
foo.push("Test") # We first have to push an item so that we'll have something to pop
print(foo.pop()) # Should return the popped item, which is "Test"
print(foo.pop()) # Should return None, since there's nothing left in the stack