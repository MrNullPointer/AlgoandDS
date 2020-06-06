# Use this class as the nodes in your linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, head):
        self.head = head

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = Node(value)


def merge(list1, list2):
    # TODO: Implement this function so that it merges the two linked lists in a single, sorted linked list.

    # check if any of the input list is none
    if list1.head.value is None or list2.head.value is None:
        if list1.head.value is None:
            return list2
        if list2.head.value is None:
            return list1

    # declare an empty list
    list0 = LinkedList(None)

    #declare node 1 and node2
    node1 = list1.head
    node2 = list2.head

    # loop forever
    while True:
        # check if node 1 is greater than node 2
        if node1 and node2:
            if node1.value > node2.value:
                list0.append(node2.value)
                node2 = node2.next
            elif node2.value > node1.value:
                list0.append(node1.value)
                node1 = node1.next
            else:
                list0.append(node1.value)
                list0.append(node2.value)
                node1 = node1.next
                node2 = node2.next

        elif node1 and not node2:
            node0 = list0.head
            while node0.next:
                node0 = node0.next
            node0.next = node1
            break

        elif node2 and not node1:
            node0 = list0.head
            while node0.next:
                node0 = node0.next
            node0.next = node2
            break

        else:
            break

    return list0

        # if node 2 is greater than node 1

        # node 1 is none and node 2 has value

        # node2 is none and node 1 has value

        # both are none: break

# class NestedLinkedList(LinkedList):
#     def flatten(self):
#         return self._flatten(self.head)
#
#     def _flatten(self, node):
#         if node.next is None:
#             return merge(node.value, None)
#         return merge(node.value, self._flatten(node.next))
#         # TODO: Implement this method to flatten the linked list in ascending sorted order.


# linked_list = LinkedList(Node(1))
# linked_list.append(Node(3))
# linked_list.append(Node(5))
#
# nested_linked_list = NestedLinkedList(Node(linked_list))
#
# second_linked_list = LinkedList(Node(2))
# second_linked_list.append(4)
#
# nested_linked_list.append(Node(second_linked_list))
#
# solution = nested_linked_list.flatten()
# assert solution == [1,2,3,4,5]




list1 = LinkedList(Node(1))
list1.append(4)
list1.append(6)

list3 = LinkedList(Node(None))

list2 = LinkedList(Node(2))
list2.append(3)

merged_list = (merge(list3,list2))
print("Hello")