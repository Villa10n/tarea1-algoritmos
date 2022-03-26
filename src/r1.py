import numpy as np

numeroReinas = int(input("Numero de reinas: "))
matriz = np.zeros((numeroReinas, numeroReinas))

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

posX = int(input("X: "))
posY = int(input("Y: "))
colocarReina(posX, posY)
print(matriz)