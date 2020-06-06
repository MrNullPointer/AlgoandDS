'''
Task 1: Create a Node class

Task 2: In the cell below, see if you can write the __init__ method for our Stack class. It will need two attributes:
A head attribute to keep track of the first node in the linked list
A num_elements attribute to keep track of how many items are in the stack

Task 3: Add the push method:
The method will need to have a parameter for the value that you want to push
You'll then need to create a new Node object with this value and link it to the list
Remember that we want to add new items at the head of the stack, not the tail!
Once you've added the new node, you'll want to increment num_elements

Task 4: Add is_empty and size methods

Task 5: Add pop method
'''

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.num_elements = 0

    def push(self,value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.num_elements += 1
        return None

    def is_empty(self):
        return self.num_elements == 0

    def size(self):
        return self.num_elements

    def pop(self):
        if self.is_empty():
            return None
        val = self.head.value
        self.head = self.head.next
        self.num_elements -= 1
        return val


# Setup
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)

# Test size
print ("Pass" if (stack.size() == 5) else "Fail")

# Test pop
print ("Pass" if (stack.pop() == 50) else "Fail")

# Test push
stack.push(60)
print ("Pass" if (stack.pop() == 60) else "Fail")
print ("Pass" if (stack.pop() == 40) else "Fail")
print ("Pass" if (stack.pop() == 30) else "Fail")
stack.push(50)
print ("Pass" if (stack.size() == 3) else "Fail")