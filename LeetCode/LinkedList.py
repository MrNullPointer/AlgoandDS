class LinkedNode(object):
    def __init__(self,x):
        self.value = x
        self.next = None

class LinkedList(object):
    size = 0
    def __init__(self,x):
        self.node = LinkedNode(x)
        LinkedList.size += 1

    def addNode(self,x):
        '''adding a new node to the linked list'''
        if self.node.next == None:
            self.node.next = LinkedNode(x)
        else:
            '''finding the next empty place to insert the node'''
            while(True):
                if self.node.next == None:
                    self.node.next = LinkedNode(x)
                    break
                else:
                    self.node = self.node.next

        LinkedList.size += 1

x = LinkedList(1)
x.addNode(1)
x.addNode(2)
x.addNode(3)
x.addNode(4)
