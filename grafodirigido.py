class Nodo(object):

 def __init__(self, n):
  self.nombre = n
  self.nodos = list()
 def agregar_nodo(self, v):
  if v not in self.nodos:
   self.nodos.append(v)
   self.nodos.sort()

class Grafo(object):

 grafnodos = {}

 def agregarNodo(self, nod):
  if isinstance(nod, Nodo) and nod.nombre not in self.grafnodos:
   self.grafnodos[nod.nombre] = nod
   return True
  else:
   return False

 def agregarBorde(self, u, v):
  if u in self.grafnodos and v in self.grafnodos:
   self.grafnodos[u].agregar_nodo(v)
   self.grafnodos[v].agregar_nodo(u)
   return True
  else:
   return False

 def imprimir(self):
  for key in sorted(list(self.grafnodos.keys())):
   print(key + str(self.grafnodos[key].nodos))

if __name__ == '__main__':
 g = Grafo()
 for i in range(ord('1'), ord('6')):
  g.agregarNodo(Nodo(chr(i)))

 bordes = ['12','26','65','52','45','23']

 for borde in bordes:
  g.agregarBorde(borde[:1],borde[1:])

 g.imprimir()