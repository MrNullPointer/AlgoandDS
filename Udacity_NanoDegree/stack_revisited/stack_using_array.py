'''
push - adds an item to the top of the stack
pop - removes an item from the top of the stack (and returns the value of that item)
size - returns the size of the stack
top - returns the value of the item at the top of stack (without removing that item)
is_empty - returns True if the stack is empty and False otherwise
'''

class Stack(object):
    def __init__(self,size = 10):
        self.arr = [0 for _ in range(size)]
        self.next_index = 0
        self.num_elements = 0

    def push(self,val):
        if self.next_index == len(self.arr):
            self._handle_stack_full_capacity()
        self.arr[self.next_index] = val
        self.num_elements += 1
        self.next_index += 1

    def _handle_stack_full_capacity(self):
        old_stack = self.arr
        self.arr = [1 for _ in range(2*len(old_stack))]

        for idx,val in enumerate(old_stack):
            self.arr[idx] = val

    def top(self):
        if self.next_index == 0:
            return
        return self.arr[self.next_index - 1]

    def size(self):
        return self.num_elements

    def pop(self):
        if self.next_index == 0:
            return
        self.next_index -= 1
        self.num_elements -= 1
        return self.arr[self.next_index]

    def is_empty(self):
        return self.num_elements  == 0

stack = Stack()
y = stack.is_empty()
for val in range(10):
    stack.push(val)

x = stack.pop()
print(x)

stack.push("Gello")
stack.push("Hi")
z = stack.is_empty()


print("Done")
