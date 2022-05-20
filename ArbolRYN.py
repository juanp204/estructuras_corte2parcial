class Node:
    def __init__(self, val, color="R"):
        self.val = val
        self.color = color
        self.left = None
        self.right = None
        self.parent = None
 
    def is_black_node(self):
        return self.color == "B"
 
    def set_black_node(self):
        self.color = "B"
 
    def set_red_node(self):
        self.color = "R"
 
    def print(self):
        if self.left:
            self.left.print()
        print(self.val)
        if self.right:
            self.right.print()


class RBTree:
    def __init__(self):
        self.root = None
    

    def left_rotate(self, node):
        parent = node.parent
        right = node.right
        node.right = right.left
        if node.right:
            node.right.parent = node
        right.left = node
        node.parent = right
        right.parent = parent
        if not parent:
            self.root = right
        else:
            if parent.left == node:
                parent.left = right
            else:
                parent.right = right
 
 
    def right_rotate(self, node):
        parent = node.parent
        left = node.left
        node.left = left.right
        if node.left:
            node.left.parent = node
        left.right = node
        node.parent = left
        left.parent = parent
        if not parent:
            self.root = left
        else:
            if parent.left == node:
                parent.left = left
            else:
                parent.right = left

    def print(self):
        if self.root:
            self.root.print()
