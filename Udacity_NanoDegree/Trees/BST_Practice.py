from collections import deque

class Node(object):
    ''' Node class To construct a node
    '''
    def __init__(self,value = None):
        self.value = value
        self.left = None
        self.right = None

    def get_value(self):
        return self.value
    def get_left_child(self):
        return self.left
    def get_right_child(self):
        return self.right

    def set_value(self,value):
        self.value = value
    def set_left_child(self,node):
        self.left = node
    def set_right_child(self,node):
        self.right = node

    def has_left_child(self):
        return self.left is not None
    def has_right_child(self):
        return self.right is not None

    def __repr__(self):
        return f"Node({self.get_value()})"

    def __str__(self):
        return f"Node({self.get_value()})"

class Queue(object):
    '''
    Queue class for BFS implementation
    '''
    def __init__(self):
        self.que = deque()

    def enq(self,value):
        self.que.appendleft(value)
    def deq(self):
        if len(self.que) > 0:
            return self.que.pop()
        else:
            return None
    def __len__(self):
        return len(self.que)


class Tree():
    def __init__(self):
        self.root = None

    def set_root(self, value):
        self.root = Node(value)

    def get_root(self):
        return self.root

    def compare(self, node, new_node):
        """
        0 means new_node equals node
        -1 means new node less than existing node
        1 means new node greater than existing node
        """
        if new_node.get_value() == node.get_value():
            return 0
        elif new_node.get_value() < node.get_value():
            return -1
        else:
            return 1

    """
    define insert here
    can use a for loop (try one or both ways)
    """

    def insert_with_loop(self, new_value):
        # check if the root is empty or not
        if self.get_root() is None:
            self.root = Node(new_value)
            return
        # if the root is not None, initialize a node to keep track of the operations
        node = self.root
        new_node = Node(new_value)
        # construct a while loop
        while True:
            # compare (left condition)
            if self.compare(node,new_node) == -1:
                # check if left is empty
                if node.left is None:
                    node.left = new_node
                    break
                else:
                    node = node.left

            # compare right condition
            elif self.compare(node,new_node) == 1:
                # check if right is empty
                if node.right is None:
                    node.right = new_node
                    break
                else:
                    node = node.right

            # else condition, replace the value of node
            else:
                break

    """
    define insert here (can use recursion)
    try one or both ways
    """

    def insert_with_recursion(self, value):
        # base case: if root is None: set the root to the required value
        if self.root is None:
            self.root = Node(value)
        return self.insert_recursively(self.root,Node(value))

    def insert_recursively(self,root,new_node):
        #node = root
        if self.compare(root,new_node) == 1:
            if root.right is None:
               root.right = new_node
            else:
                self.insert_recursively(root.right,new_node)
        elif self.compare(root,new_node) == -1:
            if root.left is None:
                root.left = new_node
            else:
                self.insert_recursively(root.left,new_node)
        else:
            root.set_value(new_node.get_value())
        return


    def __repr__(self):
        level = 0
        q = Queue()
        visit_order = list()
        node = self.get_root()
        q.enq((node, level))
        while (len(q) > 0):
            node, level = q.deq()
            if node == None:
                visit_order.append(("<empty>", level))
                continue
            visit_order.append((node, level))
            if node.has_left_child():
                q.enq((node.get_left_child(), level + 1))
            else:
                q.enq((None, level + 1))

            if node.has_right_child():
                q.enq((node.get_right_child(), level + 1))
            else:
                q.enq((None, level + 1))

        s = "Tree\n"
        previous_level = -1
        for i in range(len(visit_order)):
            node, level = visit_order[i]
            if level == previous_level:
                s += " | " + str(node)
            else:
                s += "\n" + str(node)
                previous_level = level

        return s



# tree = Tree()
# tree.insert_with_loop(5)
# tree.insert_with_loop(6)
# tree.insert_with_loop(4)
# tree.insert_with_loop(2)
# tree.insert_with_loop(5) # insert duplicate
# print(tree)

tree = Tree()
tree.insert_with_recursion(5)
tree.insert_with_recursion(6)
tree.insert_with_recursion(4)
tree.insert_with_recursion(2)
tree.insert_with_recursion(5) # insert duplicate
print(tree)
