class Stack:
    def __init__(self,size = 10):
        self.items = [0 for _ in range(size)]
        self.next_elem = 0
        self.total_size = 0

    def size(self):
        return self.total_size

    def is_empty(self):
        return self.total_size == 0


    def push(self, item):
        if self.next_elem == len(self.items):
            print("Stack full, Increasing stack......")
            self._handle_stack_full_capacity()

        self.items[self.next_elem] = item
        self.next_elem += 1
        self.total_size += 1

        return None

    def _handle_stack_full_capacity(self):
        old_stack = self.items
        self.items = [0 for _ in range(3 * len(old_stack))]

        for index,value in enumerate(old_stack):
            self.items[index] = value
        return None

    def pop(self):
        if self.next_elem == 0:
            return None
        self.next_elem -= 1
        self.total_size -= 1
        return self.items[self.next_elem]


MyStack = Stack()

MyStack.push("Web Page 1")
MyStack.push("Web Page 2")
MyStack.push("Web Page 3")

print (MyStack.items)

MyStack.pop()
MyStack.pop()

print ("Pass" if (MyStack.items[0] == 'Web Page 1') else "Fail")

MyStack.pop()

print ("Pass" if (MyStack.pop() == None) else "Fail")