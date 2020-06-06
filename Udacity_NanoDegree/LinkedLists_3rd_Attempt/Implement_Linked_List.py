class Node(object):
    def __init__(self,val = None):
        self.val = val
        self.next = None


class Linked_lists(object):
    def __init__(self):
        self.head = None

    def add_node(self,val):
        if self.head is None:
            self.head = Node(val)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(val)


def create_linked_list(input_list):
    if input_list is None:
        return
    linked = Linked_lists()
    for val in input_list:
        linked.add_node(val)
    return linked

#Testing:

linked_list = Linked_lists()
linked_list.add_node(2)
linked_list.add_node(3)
linked_list.add_node(4)

#print function
node = linked_list.head
while node:
    print(node.val)
    node = node.next
