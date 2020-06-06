# this code makes the tree that we'll traverse

from collections import deque


class Queue():
    def __init__(self):
        self.q = deque()

    def enq(self, value):
        self.q.appendleft(value)

    def deq(self):
        if len(self.q) > 0:
            return self.q.pop()
        else:
            return None

    def __len__(self):
        return len(self.q)

    def __repr__(self):
        if len(self.q) > 0:
            s = "<enqueue here>\n_________________\n"
            s += "\n_________________\n".join([str(item) for item in self.q])
            s += "\n_________________\n<dequeue here>"
            return s
        else:
            return "<queue is empty>"

class Node(object):

    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_left_child(self, left):
        self.left = left

    def set_right_child(self, right):
        self.right = right

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None

    def has_right_child(self):
        return self.right != None

    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node({self.get_value()})"

    def __str__(self):
        return f"Node({self.get_value()})"



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
        node = self.get_root()
        new_node = Node(new_value)

        if node is None:
            self.root = new_node
            return

        while True:
            if node.get_value() > new_value:
                 if node.has_left_child() is False:
                    node.left = new_node
                    break
                 node = node.left
                 continue
            elif node.get_value() < new_value:
                if node.has_right_child() is False:
                    node.right = new_node
                    break
                node = node.right
                continue
            else:
                node.set_value = new_value
                break


    """
    define insert here (can use recursion)
    try one or both ways
    """
    def insert_recursion(self,node,new_node):
        if self.compare(node,new_node) == -1:
            if node.has_left_child() is False:
                node.left = new_node
                return
            else:
                self.insert_recursion(node.left,new_node)
        elif self.compare(node,new_node) == 1:
            if node.has_right_child() is False:
                node.right = new_node
                return
            else:
                self.insert_recursion(node.right,new_node)
        else:
            node.set_value = new_node.get_value
            return


    def insert_with_recursion(self, value):
        if self.root is None:
            self.root = Node(value)
            return
        node = self.root
        new_node = Node(value)
        return self.insert_recursion(node,new_node)

    ### Delete Cases

    def delete_case_2_l(self,node,node_delete):  # node to be deleted has a left child
        pass
    def delete_case_2_r(self,node,node_delete):
        pass
    def delete_case_3_l(self,node,node_delete):
        pass
    def delete_case_3_r(self,node,node_delete):
        pass

    def delete(self,val):
        if self.search(val) is False:
            return -1
        new_node = Node(val)
        node = self.root
        if node.get_value() == val:   # Delete root
            if not node.has_left_child() and not node.has_right_child():
                return None
            elif node.has_left_child() and not node.has_right_child():
                self.root = node.get_left_child()
                return
            elif node.has_right_child() and not node.has_left_child():
                self.root = node.get_right_child()
                return
            else:
                return self.delete_case_3(node,new_node)

        left_right = 0  # -1 when left node has to be deleted and +1 when the right node has to be deleted
        while True:
            if node is None:
                break
            compare = self.compare(node,new_node)
            if compare == 1:
                compare_right = self.compare(node.get_right_child(),new_node)
                if compare_right == 0:
                    left_right = 1
                    break
                else:
                    node = node.get_right_child()
            elif compare == -1:
                compare_left = self.compare(node.get_left_child(),new_node)
                if compare_left == 0:
                    left_right = -1
                    break
                else:
                    node = node.get_left_child()
            else:
                return -1

        if left_right == -1:    # left child case
            node_delete = node.get_left_child()
            if node_delete.has_left_child() and node_delete.has_right_child():
                return self.delete_case_3(node,node_delete)
            elif node_delete.has_left_child() and not node_delete.has_right_child():
                return self.delete_case_2_l(node,node_delete)
            elif node_delete.has_right_child() and not node_delete.has_left_child():
                return self.delete_case_2_r(node,node_delete)
            else:
                node.set_left_child(None)
        elif left_right == 1:  # Right child case
            node_delete = node.get_right_child()
            if node_delete.has_right_child() and node_delete.has_left_child():
                return self.delete_case_3(node,node_delete)
            elif node_delete.has_right_child() and not node_delete.has_left_child():
                return self.delete_2_r(node,node_delete)
            elif node_delete.has_left_child() and not node_delete.has_right_child():
                return self.delete_2_l(node,node_delete)
            else:
                node.set_right_child(None)
        return



    """
        implement search
        """

    def search(self, value):
        node = self.root
        new_node = Node(value)
        while True:
            if node is None:
                break
            compare = self.compare(node,new_node)
            if compare == -1:
                if node.has_left_child() is False:
                    return False
                else:
                    node = node.get_left_child()
                    continue
            if compare == 1:
                if node.has_right_child() is False:
                    return False
                else:
                    node = node.get_right_child()
                    continue
            else:
                return True
        return False

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
tree.insert_with_recursion(3)
tree.insert_with_recursion(4)
tree.insert_with_recursion(7)
tree.insert_with_recursion(6)
tree.insert_with_recursion(10) # insert duplicate
tree.insert_with_recursion(9)
tree.insert_with_recursion(8)
tree.insert_with_recursion(8.5)
# print(tree)

tree.delete(7.5)

print(f"""
search for 8: {tree.search(8)}
search for 2: {tree.search(2)}
search for 5: {tree.search(5)}
""")
print(tree)
