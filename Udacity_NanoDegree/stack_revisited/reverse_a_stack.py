class LinkedListNode(object):
    def __init__(self,val):
        self.data = val
        self.next = None

class Stack(object):
    def __init__(self):
        self.head = None
        self.num_elements = 0

    def push(self,val):
        node = LinkedListNode(val)
        if self.head is None:
            self.head  = node
            self.num_elements += 1
            return
        node.next = self.head
        self.head = node
        self.num_elements += 1

    def pop(self):
        if self.head is None:
            return
        temp = self.head.data
        self.head  = self.head.next
        self.num_elements -= 1
        return temp

    def top(self):
        if self.head is None:
            return
        return self.head.data

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

def reverse_stack(stack):
    """
    Reverse a given input stack

    Args:
       stack(stack): Input stack to be reversed
    Returns:
       stack: Reversed Stack
    """
    if stack.is_empty():
        return
    rev_stack = Stack()
    while not stack.is_empty():
        rev_stack.push(stack.pop())
    return rev_stack


def test_function(test_case):
    stack = Stack()
    for num in test_case:
        stack.push(num)

    reverse_stack(stack)
    index = 0
    while not stack.is_empty():
        popped = stack.pop()
        if popped != test_case[index]:
            print("Fail")
            return
        else:
            index += 1
    print("Pass")

test_case_1 = [1, 2, 3, 4]
test_function(test_case_1)

test_case_2 = [1]
test_function(test_case_2)