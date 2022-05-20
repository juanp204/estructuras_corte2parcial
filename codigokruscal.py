class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def agregar_nodo(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def apply_union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    #  Applying Kruskal algorithm
    def kruskal_algo(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
        for u, v, weight in result:
            print("%d - %d: %d" % (u, v, weight))


g = Graph(8)
g.agregar_nodo(0, 2, 5)
g.agregar_nodo(2, 0, 5)
g.agregar_nodo(0, 1, 3)
g.agregar_nodo(1, 0, 3)
g.agregar_nodo(0, 7, 10)
g.agregar_nodo(7, 0, 10)
g.agregar_nodo(0, 3, 2)
g.agregar_nodo(3, 0, 2)
g.agregar_nodo(1, 2, 5)
g.agregar_nodo(2, 1, 5)
g.agregar_nodo(1, 6, 6)
g.agregar_nodo(6, 1, 6)
g.agregar_nodo(1, 3, 8)
g.agregar_nodo(3, 1, 8)
g.agregar_nodo(1, 4, 4)
g.agregar_nodo(4, 1, 4)
g.agregar_nodo(1, 7, 6)
g.agregar_nodo(7, 1, 6)
g.agregar_nodo(2, 5, 7)
g.agregar_nodo(5, 2, 7)
g.agregar_nodo(2, 6, 9)
g.agregar_nodo(6, 2, 9)
g.agregar_nodo(2, 4, 1)
g.agregar_nodo(4, 2, 1)
g.agregar_nodo(3, 4, 12)
g.agregar_nodo(4, 3, 12)
g.agregar_nodo(3, 7, 14)
g.agregar_nodo(7, 3, 14)
g.agregar_nodo(4, 5, 15)
g.agregar_nodo(5, 4, 15)
g.agregar_nodo(5, 7, 9)
g.agregar_nodo(7, 5, 9)
g.agregar_nodo(6, 7, 3)
g.agregar_nodo(7, 6, 3)
g.kruskal_algo() 