'''Linked list implementation from udacity course'''

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

def printNode(head):
    current_node = head

    while current_node is not None:
        print(current_node.value)
        current_node = current_node.next

    return None

# def create_linked_list(input_list):    # This is a O(n^2) approach
#     """
#     Function to create a linked list
#     @param input_list: a list of integers
#     @return: head node of the linked list
#     """
#     head = None
#     new_node = None
#
#     for num in input_list:
#         new_node = Node(num)
#         if head == None:
#             head = new_node
#         else:
#             current_Node = head
#             while current_Node.next:
#                 current_Node = current_Node.next
#             current_Node.next = new_node
#     return head

def create_linked_list_better(input_list):   # This is the better version of previous implementation with complexity O(n)
    head = None
    tail = None

    for num in input_list:
        if head is None:
            head = Node(num)
            tail = head
        else:
            tail.next = Node(num)
            tail = tail.next

    return head

# head = Node(2)
# head.next = Node(1)
# head.next.next = Node(4)
# head.next.next.next = Node(3)
# head.next.next.next.next = Node(5)

head = create_linked_list_better([3,4,5,6,7,8,9,9])

printNode(head)



# print(head.value)
# print(head.next.value)
# print(head.next.next.value)
# print(head.next.next.next.value)
# print(head.next.next.next.next.value)
