import heapq
import sys

class Graph:
    
    def __init__(self):
        self.nodos = {}
        
    def agregar_nodo(self, name, edges):
        self.nodos[name] = edges
    
    def encontrar_camino(self, start, finish):
        rutas = {} 
        anterior = {} 
        nodes = [] 

        for nodo in self.nodos:
            if nodo == start:
                rutas[nodo] = 0
                heapq.heappush(nodes, [0, nodo])
            else:
                rutas[nodo] = sys.maxsize
                heapq.heappush(nodes, [sys.maxsize, nodo])
            anterior[nodo] = None
        
        while nodes:
            pequeño = heapq.heappop(nodes)[1] 
            if pequeño == finish: 
                path = []
                while anterior[pequeño]: 
                    path.append(pequeño)
                    pequeño = anterior[pequeño]
                return path
            if rutas[pequeño] == sys.maxsize:
                break
            
            for vecino in self.nodos[pequeño]: 
                alt = rutas[pequeño] + self.nodos[pequeño][vecino] 
                if alt < rutas[vecino]: 
                    rutas[vecino] = alt
                    anterior[vecino] = pequeño
                    for n in nodes:
                        if n[1] == vecino:
                            n[0] = alt
                            break
                    heapq.heapify(nodes)
        return rutas
        
    def __str__(self):
        return str(self.nodos)
    
if __name__ == '__main__':
    g = Graph()
    g.agregar_nodo('A', {'B': 4, 'C': 3})
    g.agregar_nodo('B', {'A': 4, 'D': 5})
    g.agregar_nodo('C', {'A': 3, 'D': 1, 'F': 2})
    g.agregar_nodo('D', {'B': 5, 'C': 1, 'F': 2})
    g.agregar_nodo('E', {'D': 3, 'H': 2, 'G': 6})
    g.agregar_nodo('F', {'C': 2, 'D': 2, 'H': 5})
    g.agregar_nodo('G', {'B': 1, 'E': 6})
    g.agregar_nodo('H', {'E': 2, 'F': 5})
    print(g.encontrar_camino('A', 'H'))