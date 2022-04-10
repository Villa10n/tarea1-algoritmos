import numpy as np

numeroReinas = int(input("Numero de reinas: "))
matriz = np.zeros((numeroReinas, numeroReinas))
posiciones = []

def colocarReina(x, y):
    # Llenado horizontal
    for i in range(numeroReinas):
        matriz[x][i] = 1
    # Llenado vertical
    for j in range(numeroReinas):
        matriz[j][y] = 1
    # Diagonal cuadrante 1
    c1x = x
    c1y = y
    for c1 in range(y, len(matriz[0])):    
        if (c1x == 0 or c1y == len(matriz[0]) - 1):
            break
        c1x -= 1
        c1y += 1
        matriz[c1x][c1y] = 1
    # Diagonal cuadrante 2
    c2x = x
    c2y = y
    for c2 in range(0, y):    
        if (c2x == 0 or c2y == 0):
            break
        c2x -= 1
        c2y -= 1
        matriz[c2x][c2y] = 1
    # Diagonal cuadrante 3
    c3x = x
    c3y = y
    for c3 in range(0, y):    
        if (c3x == numeroReinas - 1 or c3y == 0):
            break
        c3x += 1
        c3y -= 1
        matriz[c3x][c3y] = 1
    # Diagonal cuadrante 4
    c4x = x
    c4y = y
    for c4 in range(y, numeroReinas):    
        if (c4x == numeroReinas - 1 or c4y == numeroReinas - 1):
            break
        c4x += 1
        c4y += 1
        matriz[c4x][c4y] = 1
    matriz[x][y] = 2

def recorrerColumna(y):
    seAgrega = False
    for i in range(0, numeroReinas):
        print("marca: ", i, ",", y)
        if (matriz[i][y] == 0):
            print("Posicion a guardar: ", i, ",", y)
            posiciones.append([y, i])
            seAgrega = True
    return seAgrega

def setear():
    x = posiciones[len(posiciones) - 1][1]
    y = posiciones[len(posiciones) - 1][0]
    posiciones.pop()
    return [y, x]

def buscarSolucionM2():
    ver = 0
    columna = 0
    contador = 0
    reinasColocadas = 0
    while (contador != numeroReinas):
        if (ver == 6):
            break
        # Buscar posiciones en la columna
        seAgrega = recorrerColumna(columna)
        if (seAgrega == False and columna < numeroReinas):
            columna += 1
            continue
        # setear
        posXY = setear()
        x = posXY[1]
        y = posXY[0]
        # Colocamos la reina
        print("---------------------Reina colocada en: ", x, ",", y)
        colocarReina(x, y)
        contador += 1
        columna += 1
        ver += 1
        print(matriz)

buscarSolucionM2()
print("Posiciones: ", posiciones)