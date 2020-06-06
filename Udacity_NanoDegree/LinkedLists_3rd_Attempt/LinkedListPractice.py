'''

    Append data to the tail of the list and prepend to the head
    Search the linked list for a value and return the node
    Remove a node
    Pop, which means to return the first node's value and delete the node from the list
    Insert data at some position in the list
    Return the size (length) of the linked list

'''


class Node(object):
    def __init__(self, val=None):
        self.value = val
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None

    def to_list(self):
        out = list()
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out

    def prepend(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)
        return


def search(self, value):
    if self.head is None:
        return
    node = self.head
    while node and node.value != value:
        node = node.next
    if node is None:
        return -1
    else:
        return node

def remove(self, value):
    """ Remove first occurrence of value. """
    # TODO: Write function to remove here
    if self.head is None:
        return
    node = self.head
    if node.value == value:
        self.head = node.next
        return
    while node.next and node.next.value != value:
        node = node.next
    if node.next.value == value:
        node.next = node.next.next
    return

def pop(self):
    """ Return the first node's value and remove it from the list. """
    # TODO: Write function to pop here
    if self.head is None:
        return
    node = self.head
    self.head = self.head.next
    return node.value

def size(self):
    """ Return the size or length of the linked list. """
    # TODO: Write function to get size here
    count = 0
    node = self.head
    while node:
        count += 1
        node = node.next
    return count


def insert(self, value, pos):
    """ Insert value at pos position in the list. If pos is larger than the
    length of the list, append to the end of the list. """

    # TODO: Write function to insert here
    if self.head is None:
        self.head == Node(value)
        return
    count = 0
    node = self.head
    if pos == 0:
        self.prepend(value)
    elif pos >= self.size():
        self.append(value)
    else:
        while count < pos-1:
            node = node.next
            count += 1
        temp = node.next
        node.next = Node(value)
        node.next.next = temp
    return




LinkedList.insert = insert
LinkedList.size = size
LinkedList.pop = pop
LinkedList.remove = remove
LinkedList.search = search
# ----------------------------------Testing--------------------------------------------------#
# # Test prepend
# linked_list = LinkedList()
# linked_list.prepend(1)
# assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
# # Test append - 1
# linked_list.append(3)
# linked_list.prepend(2)
# assert linked_list.to_list() == [2, 1, 3], f"list contents: {linked_list.to_list()}"

# Test append - 2
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


