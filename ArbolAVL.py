class Node:
    def __init__(self, valor):
        self.valor = valor
        self.nparent = None
        self.nleft = None
        self.nright = None
        self.height = 0

    def right(self):
        return self.nright

    def right(self, node):
        if node is not None:
            node._parent = self
            self.nright = node

    def left(self):
        return self.nleft

    def left(self, node):
        if node is not None:
            node._parent = self
            self.nleft = node

    def parent(self):
        return self.nparent

    def parent(self, node):
        if node is not None:
            self.nparent = node
            self.height = self.parent.height + 1
        else:
            self.height = 0

class AVL:

    def __init__(self):
        self.root = None
        self.size = 0

    def agregar_nodo(self, value):
        node = Node(value)

        if self.root is None:
            self.root = node
            self.root.height = 0
            self.size = 1
        else:
            nodo_padre = None
            nodo = self.root

            while True:
                if nodo is not None:

                    nodo_padre = nodo

                    if node.valor < nodo.valor:
                        nodo = nodo.left
                    else:
                        nodo = nodo.right
                else:
                    node.height = nodo_padre.height
                    nodo_padre.height += 1
                    if node.valor < nodo_padre.valor:
                        nodo_padre.left = node
                    else:
                        nodo_padre.right = node
                    self.rebalance(node)
                    self.size += 1
                    break


    def rebalance(self, nodo):
        n = nodo
        while n is not None:
            height_right = n.height
            height_left = n.height

            if n.right is not None:
                height_right = n.right.height

            if n.left is not None:
                height_left = n.left.height

            if abs(height_left - height_right) > 1:
                if height_left > height_right:
                    left_child = n.left
                    if left_child is not None:
                        h_right = (left_child.right.height
                                    if (left_child.right is not None) else 0)
                        h_left = (left_child.left.height
                                    if (left_child.left is not None) else 0)
                    if (h_left > h_right):
                        self.rotar_left(n)
                        break
                    else:
                        self.double_rotate_right(n)
                        break
                else:
                    right_child = n.right
                    if right_child is not None:
                        h_right = (right_child.right.height
                            if (right_child.right is not None) else 0)
                        h_left = (right_child.left.height
                            if (right_child.left is not None) else 0)
                    if (h_left > h_right):
                        self.double_rotate_left(n)
                        break
                    else:
                        self.rotar_right(n)
                        break
            n = n.parent

    def rotar_left(self, nodo):
        aux = nodo.parent.valor
        nodo.parent.valor = nodo.valor
        nodo.parent.right = Node(aux)
        nodo.parent.right.height = nodo.parent.height + 1
        nodo.parent.left = nodo.right


    def rotar_right(self, nodo):
        aux = nodo.parent.valor
        nodo.parent.valor = nodo.valor
        nodo.parent.left = Node(aux)
        nodo.parent.left.height = nodo.parent.height + 1
        nodo.parent.right = nodo.right

    def double_rotate_left(self, nodo):
        self.rotar_right(nodo.right().right())
        self.rotar_left(nodo)

    def double_rotate_right(self, nodo):
        self.rotar_left(nodo.left().left())
        self.rotar_right(nodo)

    def empty(self):
        if self.root is None:
            return True
        return False

    def imprimir(self, nodo):
        if nodo is not None:
            self.imprimir(nodo.left)
            print(nodo.valor, end=" ")
            self.imprimir(nodo.right)

    def imprimir_preorder(self, nodo):
        if nodo is not None:
            self.imprimir(nodo.left)
            self.imprimir(nodo.right)
            print(nodo.valor, end=" ")


if __name__ == '__main__':
    t = AVL()
    t.agregar_nodo(148)
    t.agregar_nodo(13)
    t.agregar_nodo(49)
    t.agregar_nodo(85)
    t.agregar_nodo(60)
    t.agregar_nodo(99)
    t.agregar_nodo(35)
    t.agregar_nodo(58)
    t.agregar_nodo(10)
    t.imprimir_preorder(t.root)