def prim(matriz,numnodos,nodoi):
    nodos = []
    while(len(nodos) != numnodos):
        nodos.append(0)
    nodos[nodoi] = 1
    E1 = []
    distancia = 0
    for i in range(0,numnodos-1):
        minimo = 9
        agregar_nodo = 0
        e = []
        for j in range(0, numnodos):
            if(nodos[j] == 1):
                for k in range(0,numnodos):
                    if(nodos[k] == 0 and matriz[j][k] < minimo):
                        agregar_nodo = k
                        e = [j,k]
                        minimo = matriz[j][k]
        distancia += matriz[e[0]][e[1]]
        nodos[agregar_nodo] = 1
        E1.append(e)

    return ["la suma de las dustancias es ", distancia]


w = [ #0,1,2,3,4           #9 ---> No existe la arista que conecta esos vertices
      [9,2,5,9,6], #0
      [2,9,5,3,2], #1
      [5,5,9,9,4], #2
      [9,3,9,9,4], #3
      [6,2,4,4,9]  #4
]

print(prim(w,5,0))
