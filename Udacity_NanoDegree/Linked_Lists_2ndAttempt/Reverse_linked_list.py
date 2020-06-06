class Node(object):
    def __init__(self, value = None):
        self.value = value
        self.next = None

class linked_list(object):
    def __init__(self):
        self.head = None

    def append(self,value):
        if self.head is None:
            self.head = Node(value)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(value)

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

    def __repr__(self):
        return str([val for val in self])


def reverse(linked):
    if linked.head is None or linked.head.next is None:
        return linked.head

    new_linked_list = linked_list()
    node = linked.head
    list_of_node_value = list()
    while node:
        list_of_node_value.append(node.value)
        node = node.next
    for val in range(len(list_of_node_value) -1 ,-1,-1):
        new_linked_list.append(list_of_node_value[val])
    return new_linked_list


linked_list_ = linked_list()
x = reverse(linked_list_)
linked_list_.append(1)
x = reverse(linked_list_)
linked_list_.append(2)
x = reverse(linked_list_)
linked_list_.append(3)
x = reverse(linked_list_)

print("Done!!")