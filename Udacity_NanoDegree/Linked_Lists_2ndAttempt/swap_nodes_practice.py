class Node(object):
    def __init__(self,val = None):
        self.value = val
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None
    def append(self,val):
        if self.head is None:
            self.head = Node(val)
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(val)

def swap_nodes(head, left_index, right_index):
    node = head
    count = 0

    left_curr = None
    right_curr = None

    left_prev = None
    right_prev = None

    while node:
        if left_index == count:
            left_curr = node
        elif right_index == count:
            right_curr = node
            break
        if left_curr is None:
            left_prev = node
        right_prev = node
        node = node.next
        count += 1

    temp = left_curr.next
    left_curr.next = right_curr.next
    right_prev.next = left_curr
    right_curr.next = temp

    if left_curr == right_prev or head == left_curr:
        head = right_curr
    else:
        left_prev.next = right_curr
    return head


linked_list = LinkedList()
for i in range(10):
    linked_list.append(i)

head = swap_nodes(linked_list.head,0,9)

print("Done!!!")