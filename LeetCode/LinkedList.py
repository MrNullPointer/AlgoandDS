class Node(object):
    def __init__(self,x):
        self.val = x
        self.next = None

class List(object):
    def __init__(self):
        self.HeadVal = None

    def printing(self):
        '''Function that prints out the entire linked list'''
        printVal = self.HeadVal
        while printVal is not None:
            '''we print the linked list in this loop'''
            print(printVal.val)
            printVal = printVal.next

linked = List()
head = Node(1)
linked.HeadVal = head
e1 = Node(2)
head.next = e1
e2 = Node(3)
e1.next = e2
linked.printing()