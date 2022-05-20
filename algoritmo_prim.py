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


ejercicio = [ 
      [9,2,5,9,6], 
      [2,9,5,3,2], 
      [5,5,9,9,4], 
      [9,3,9,9,4], 
      [6,2,4,4,9]  
]

print(prim(ejercicio,5,0))
