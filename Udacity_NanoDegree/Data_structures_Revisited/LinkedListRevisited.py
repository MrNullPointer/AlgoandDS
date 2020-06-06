'''
Implementation of a singly linked list
'''

# class Node(object):
#     def __init__(self,val = None):
#         self.val = val
#         self.next = None
#
#     def set_val(self,val):
#         self.val = val
#     def get_val(self):
#         return self.val
#
#     def set_next(self,node):
#         self.next = node
#     def get_next(self):
#         return self.next
#
#
# class LinkedList(object):
#     def __init__(self):
#         self.head = None
#
#     def append(self,val):
#         if self.head is None:
#             self.head = Node(val)
#             return
#
#         node = self.head
#         while node.next:
#             node = node.next
#         node.next = Node(val)
#         return
#
#     def to_list(self):
#         #initialize an empty list
#         to_list = []
#         #initialize a node
#         node = self.head
#         #for all the elements in node push the node value back to list
#         while node:
#             to_list.append(node.get_val())
#             node = node.next
#         return to_list

'''
Implementation of doubly linked list
'''

class Node(object):
    def __init__(self,val = None):
        self.val = val
        self.next = None
        self.prev = None

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
    def append(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
            return
        node = Node(val)
        self.tail.next = node
        self.tail.next.prev = self.tail    # setting the pointer to access previous nodes
        self.tail = self.tail.next



linked_list = LinkedList()
# print(linked_list.to_list())
linked_list.append(3)
linked_list.append(5)
linked_list.append(12)
node = linked_list.head
# print(linked_list.to_list())
while node:
    print(node.val)
    node = node.next