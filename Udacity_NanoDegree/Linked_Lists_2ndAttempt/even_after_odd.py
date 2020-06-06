class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# helper function to check off value
def is_odd(node):
    if node is None:
        return
    return node.data % 2 is not 0

def even_after_odd(head):
    """
    :param - head - head of linked list
    return - updated list with all even elements are odd elements
    """
    if head is None:
        return

    node = head
    first_odd = None
    first_even = None
    second_odd = None
    second_even = None

    if is_odd(node):
        first_odd = node
    else:
        first_even = node

    while True:
        if node is None:
            return
        if is_odd(node.next):
            if first_odd:
                if node is first_odd:
                    first_odd = node.next
                    node = node.next
                else:
                    second_odd = node.next
                    node.next = second_odd.next
                    second_odd.next = first_odd.next
                    first_odd.next = second_odd
                    first_odd = second_odd
                    second_odd = None
                    if is_odd(node.next):
                        continue
                    node = node.next
            else:
                first_odd = node.next
                node.next = first_odd.next
                first_odd.next = head
                head = first_odd
                node = node.next

        else:
            first_even = node.next
            node = node.next

    return head



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
        print(head.data, end=' ')
        head = head.next
    print()


def test_function(test_case):
    head = test_case[0]
    solution = test_case[1]

    node_tracker = dict({})
    node_tracker['nodes'] = list()
    temp = head
    while temp:
        node_tracker['nodes'].append(temp)
        temp = temp.next

    head = even_after_odd(head)
    temp = head
    index = 0
    try:
        while temp:
            if temp.data != solution[index] or temp not in node_tracker['nodes']:
                print("Fail")
                return
            temp = temp.next
            index += 1
        print("Pass")
    except Exception as e:
        print("Fail")


# arr = [1, 2, 3, 4, 5, 6]
# solution = [1, 3, 5, 2, 4, 6]
#
# head = create_linked_list(arr)
# test_case = [head, solution]
# test_function(test_case)
#
# arr = [1, 3, 5, 7]
# solution = [1, 3, 5, 7]
#
# head = create_linked_list(arr)
# test_case = [head, solution]
# test_function(test_case)
#
# arr = [2, 4, 6, 8]
# solution = [2, 4, 6, 8]
# head = create_linked_list(arr)
# test_case = [head, solution]
# test_function(test_case)

arr = [2,4,6,7,8,9,11,13]
solution = [2,4,6,7,8,9,11,13]
head = create_linked_list(arr)
test_case = [head, solution]
test_function(test_case)

# arr = [1, 3, 5, 7,2]
# solution = [1, 3, 5, 7,2]
#
# head = create_linked_list(arr)
# test_case = [head, solution]
# test_function(test_case)