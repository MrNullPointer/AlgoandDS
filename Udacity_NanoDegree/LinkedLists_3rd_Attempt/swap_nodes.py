class Node:
    """LinkedListNode class to be used for this problem"""
    def __init__(self, data):
        self.data = data
        self.next = None

"""
:param: head- head of input linked list
:param: `position_one` - indicates position (index) ONE
:param: `position_two` - indicates position (index) TWO
return: head of updated linked list with nodes swapped

TODO: complete this function and swap nodes present at position_one and position_two
Do not create a new linked list
"""
def swap_nodes(head, left_index, right_index):
    left_front = right_front = left = right = None
    if head is None:
        return
    node = head
    count = 0
    if left_index == 0:
        left = node
    while node.next:
        if count == left_index - 1:
            left_front = node
            left = node.next
        elif count == right_index - 1:
            right_front = node
            right = node.next
            break
        node = node.next
        count = count + 1

    if left_front is None:   # left node is the head node
        if left == right_front: # Adjacent nodes
            left.next = right.next
            right.next = left
            head = right
        else:
            temp = left.next
            left.next = right.next
            right.next = temp
            right_front.next = left
            left_front.next = right
    elif left == right_front:
        left.next = right.next
        right.next = left
        left_front.next = right
    else:
        temp = left.next
        left.next = right.next
        right_front.next = left
        right.next = temp
        left_front.next = right
    return head







def test_function(test_case):
    head = test_case[0]
    left_index = test_case[1]
    right_index = test_case[2]

    left_node = None
    right_node = None

    temp = head
    index = 0
    try:
        while temp is not None:
            if index == left_index:
                left_node = temp
            if index == right_index:
                right_node = temp
                break
            index += 1
            temp = temp.next

        updated_head = swap_nodes(head, left_index, right_index)

        temp = updated_head
        index = 0
        pass_status = [False, False]

        while temp is not None:
            if index == left_index:
                pass_status[0] = temp is right_node
            if index == right_index:
                pass_status[1] = temp is left_node

            index += 1
            temp = temp.next

        if pass_status[0] and pass_status[1]:
            print("Pass")
        else:
            print("Fail")
        return updated_head
    except Exception as e:
        print("Fail")

# helper functions for testing purpose
def create_linked_list(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    tail = head
    for data in arr[1:]:
        tail.next = Node(data)
        tail = tail.next
    return head

def print_linked_list(head):
    while head:
        print(head.data, end=" ")
        head = head.next
    print()

arr = [3, 4, 5, 2, 6, 1, 9]
head = create_linked_list(arr)
left_index = 3
right_index = 4

test_case = [head, left_index, right_index]
updated_head = test_function(test_case)

arr = [3, 4, 5, 2, 6, 1, 9]
left_index = 2
right_index = 4
head = create_linked_list(arr)
test_case = [head, left_index, right_index]
updated_head = test_function(test_case)

arr = [3, 4, 5, 2, 6, 1, 9]
left_index = 0
right_index = 1
head = create_linked_list(arr)
test_case = [head, left_index, right_index]
updated_head = test_function(test_case)