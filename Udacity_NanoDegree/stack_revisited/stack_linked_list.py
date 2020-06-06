class Node(object):
    def __init__(self,val):
        self.value = val
        self.next = None

class Stack(object):
    def __init__(self):
        self.head = None
        self.num_elements = 0

    def push(self,val):
        if self.head is None:
            self.head = Node(val)
            self.num_elements += 1
            return
        node = Node(val)
        node.next = self.head
        self.head = node
        self.num_elements += 1

    def pop(self):
        if self.head is None:
            return
        node = self.head
        self.head = self.head.next
        self.num_elements -= 1
        return node.value

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.head is None


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


