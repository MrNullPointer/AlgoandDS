'''
. Append data to the tail of the list and prepend to the head
. Search the linked list for a value and return the node
. Remove a node
. Pop, which means to return the first node's value and delete the node from the list
. Insert data at some position in the list
. Return the size (length) of the linked list
'''

class Node(object):
    def __init__(self,val = None):
        self.value = val
        self.next = None

class Linked_list(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self,val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

    def search(self,val):
        node = self.head
        while node:
            if node.value == val:
                break
            node = node.next
        return node

    def remove(self,val):
        if self.head is None:
            return

        if self.head.value == val:
            self.head = self.head.next
            return

        node = self.head
        while node.next:
            if node.next.value == val:
                node.next = node.next.next
                break
            node = node.next

    def pop(self):
        if self.head is None:
            return
        temp_value = self.head.value
        self.head = self.head.next
        return temp_value

    def insert(self,value,pos):
        new_node = Node(value)
        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            return
        node = self.head
        count = 0
        while node.next:
            if count == pos - 1:
                new_node.next = node.next
                node.next = new_node
                break
            node = node.next
            count += 1
            if node.next is None:
                node.next = new_node
                self.tail = node.next
                break

    def size(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count




linked_list = Linked_list()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
node = linked_list.search(2)



linked_list.insert(20,50)
size = linked_list.size()

print("Done!!")