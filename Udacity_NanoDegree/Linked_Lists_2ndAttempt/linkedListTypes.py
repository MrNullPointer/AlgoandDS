class Node(object):
    def __init__(self,val = None):
        self.value = val
        self.next = None
        self.previous = None

    def get_value(self):
        return self.value
    def get_next(self):
        return self.next
    def is_next(self):
        return self.next is not None

    def set_value(self,value):
        self.value = value
    def set_next(self,node):
        self.next = node


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self,val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(val)
            node.next.previous = node

    def append_tail(self,val):
        if self.tail is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail.next.previous = self.tail
            self.tail = self.tail.next

    def pop_head(self):
        node = self.head.value
        self.head = self.head.next
        return node

    def to_list(self):
        list_linked_list = list()
        node = self.head
        while node:
            list_linked_list.append(node.value)
            node = node.next
        return list_linked_list

# Testing the implementation:

linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
Node_val = linked_list.pop_head()
print(Node_val)

another_list = LinkedList()
another_list.append_tail(1)
another_list.append_tail(2)
another_list.append_tail(3)


return_list = linked_list.to_list()


print("Done!!!")
