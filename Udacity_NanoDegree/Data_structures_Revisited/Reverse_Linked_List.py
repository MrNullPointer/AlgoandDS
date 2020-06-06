class Node(object):
    def __init__(self,value = None):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)

    def prepend(self,value):
        if self.head is None:
            self.head = Node(value)
            return
        node = Node(value)
        node.next = self.head
        self.head = node

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

def reversed_list(node):
    if node is None:
        return
    linked = LinkedList()
    val = node.value
    foo = reversed_list(node.next)
    if foo is None:
        linked.append(val)
        return linked
    linked.head = foo.head
    linked.append(val)
    return linked

def reverse(list):
    return reversed_list(list.head)


llist = LinkedList()
for value in [4,2,5,1,-3,0]:
    llist.append(value)

flipped = reverse(llist)
is_correct = list(flipped) == list([0,-3,1,5,2,4]) and list(llist) == list(reverse(flipped))
print("Pass" if is_correct else "Fail")