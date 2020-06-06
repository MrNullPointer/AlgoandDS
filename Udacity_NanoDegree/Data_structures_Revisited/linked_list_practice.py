'''
+ Append data to the tail of the list and prepend to the head
+ Search the linked list for a value and return the node
+ Remove a node
+ Pop, which means to return the first node's value and delete the node from the list
+ Insert data at some position in the list
+ Return the size (length) of the linked list
'''

class Node(object):
    def __init__(self,value = None):
        self.value = value
        self.next = None

    def set_value(self,value):
        self.value = value
    def set_next(self,node):
        self.next = node

    def get_value(self):
        return self.value
    def get_next(self):
        return self.next

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self,value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
            return
        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
        return

    def prepend(self,value):
        node = Node(value)
        node.next = self.head
        self.head = node
        if self.tail is None:
            self.tail = self.head

    def to_list(self):
        list_to_be_returned = list()
        node = self.head

        while node:
            list_to_be_returned.append(node.get_value())
            node = node.next
        return list_to_be_returned

    def search(self,value):
        node = self.head
        while node:
            if node.get_value() == value:
                return node
            node = node.next
        return

    def remove(self,value):
        if self.head is None:
            return

        if self.head.get_value() == value:
            self.head = self.head.next
            return
        node = self.head
        while node.next:
            if node.next.get_value() == value:
                node.next = node.next.next
                return
            node = node.next

    def pop(self):
        if self.head is None:
            return
        value = self.head.get_value()
        self.remove(value)
        return value

    def insert(self,value,pos):
        if pos == 0:
            node = Node(value)
            node.next = self.head
            self.head = node
            return
        node = self.head
        index = 0
        while node.next:
            if index == pos-1:
                foo = Node(value)
                foo.next = node.next
                node.next = foo
                return
            index = index + 1
            node = node.next

        self.append(value)
        return

    def size(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count


## Test your implementation here

# Test prepend
linked_list = LinkedList()
linked_list.prepend(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
linked_list.append(3)
linked_list.prepend(2)
assert linked_list.to_list() == [2, 1, 3], f"list contents: {linked_list.to_list()}"

# Test append
linked_list = LinkedList()
linked_list.append(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
linked_list.append(3)
assert linked_list.to_list() == [1, 3], f"list contents: {linked_list.to_list()}"

# Test search
linked_list.prepend(2)
linked_list.prepend(1)
linked_list.append(4)
linked_list.append(3)
assert linked_list.search(1).value == 1, f"list contents: {linked_list.to_list()}"
assert linked_list.search(4).value == 4, f"list contents: {linked_list.to_list()}"

# Test remove
linked_list.remove(1)
assert linked_list.to_list() == [2, 1, 3, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4], f"list contents: {linked_list.to_list()}"

# Test pop
value = linked_list.pop()
assert value == 2, f"list contents: {linked_list.to_list()}"
assert linked_list.head.value == 1, f"list contents: {linked_list.to_list()}"

# Test insert
linked_list.insert(5, 0)
assert linked_list.to_list() == [5, 1, 4], f"list contents: {linked_list.to_list()}"
linked_list.insert(2, 1)
assert linked_list.to_list() == [5, 2, 1, 4], f"list contents: {linked_list.to_list()}"
linked_list.insert(3, 6)
assert linked_list.to_list() == [5, 2, 1, 4, 3], f"list contents: {linked_list.to_list()}"

# Test size
assert linked_list.size() == 5, f"list contents: {linked_list.to_list()}"

