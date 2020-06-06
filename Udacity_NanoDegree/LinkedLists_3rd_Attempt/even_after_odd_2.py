class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def is_odd(node):
    return node.data % 2 == 1

def even_after_odd(head):
    """
    :param - head - head of linked list
    return - updated list with all even elements are odd elements
    """
    if head is None:
        return
    first_odd = first_even = second_odd = None
    node = head
    if is_odd(node):
        first_odd = node
    else:
        first_even = node

    while True:
        if node is None:
            break
        next_node = node.next
        if next_node:
            if is_odd(next_node):
                if node == first_odd:
                    first_odd = next_node
                    node = node.next
                elif first_odd:
                    second_odd = next_node
                    node.next = second_odd.next
                    second_odd.next = first_odd.next
                    first_odd.next = second_odd
                    node = node.next
                    first_odd = second_odd
                elif first_even and first_odd is None:
                    node.next = next_node.next
                    next_node.next = first_even
                    head = next_node
                    first_odd = next_node
                else:
                    break
            else:
                if first_even:
                    node = node.next
                else:
                    first_even = next_node
                    node = node.next
        else:
            node = node.next
    return head

def create_linked_list(arr):
    if len(arr) == 0:
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


arr = [1, 2, 3, 4, 5, 6]
solution = [1, 3, 5, 2, 4, 6]

head = create_linked_list(arr)
test_case = [head, solution]
test_function(test_case)

arr = [1, 3, 5, 7]
solution = [1, 3, 5, 7]

head = create_linked_list(arr)
test_case = [head, solution]
test_function(test_case)

arr = [2, 4, 6, 8]
solution = [2, 4, 6, 8]
head = create_linked_list(arr)
test_case = [head, solution]
test_function(test_case)

arr = [2, 4, 6, 8, 10, 12, 13, 11]
solution = [13, 11, 2, 4, 6, 8, 10, 12]
head = create_linked_list(arr)
test_case = [head, solution]
test_function(test_case)
