class Node(object):
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

class Tree(object):
    def __init__(self,val = None):
        self.root = Node(val)

    def get_root(self):
        return self.root

def in_order_traversal(tree):
    root = tree.root
    in_order_print(root)

def in_order_print(root):
    if root is None:
        return
    in_order_print(root.left)
    print(root.value)
    in_order_print(root.right)

def pre_order(tree):
    root = tree.root
    pre_order_print(root)

def pre_order_print(root):
    if root is None:
        return
    print(root.value)
    pre_order_print(root.left)
    pre_order_print(root.right)

def post_order(tree):
    root = tree.root
    post_order_print(root)

def post_order_print(root):
    if root is None:
        return
    post_order_print(root.left)
    post_order_print(root.right)
    print(root.value)

tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))
in_order_traversal(tree)
print("=========")
pre_order(tree)
print("========")
post_order(tree)
