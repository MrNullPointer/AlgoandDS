class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class linked_list:
    def __init__(self):
        self.head = None

    def append(self,value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)


linked = linked_list()
linked.append(1)
linked.append(2)
linked.append(3)
linked.append(4)

head = linked.head
while head:
    print(head.value)
    head = head.next
