from turtle import pos
import numpy as np

numeroReinas = int(input("Numero de reinas: "))
matriz = np.zeros((numeroReinas, numeroReinas))
posiciones = []
posReinasColocadas = []

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
    print("Recorriendo columna: ", y)
    for i in range(0, numeroReinas):
        if (matriz[i][y] == 0):
            print("Posicion a guardar: ", i, ",", y)
            posiciones.append([i, y])
            seAgrega = True
    return seAgrega

def setear():
    x = posiciones[len(posiciones) - 1][1]
    y = posiciones[len(posiciones) - 1][0]
    posiciones.pop()
    return [y, x]

def limpiarMatriz():
    matriz[:] = np.zeros((numeroReinas, numeroReinas))
    print("Matriz limpia: ")
    print(matriz)
    colocarNuevamente()

def colocarNuevamente():
    print("pos reinas colocadas: ", posReinasColocadas)
    for pos in posReinasColocadas:
        x = pos[1]
        y = pos[0]
        print("pos guardada", pos)
        colocarReina(y, x)
    print("Matriz nuevamente colocada: ")
    print(matriz)

def buscarSolucionM2():
    columna = 0
    contador = 0
    reinasColocadas = 0
    x = 0
    y = 0
    while (contador != numeroReinas):
        print("----------------------------------------------------")
        # Buscar posiciones en la columna
        print("Posiciones: ", posiciones)
        print("Reinas colocadas: ", posReinasColocadas)
        seAgrega = recorrerColumna(columna)
        if (seAgrega == False):
            print("No queda espacio para la reina, debemos volver...")
            if (len(posiciones) > 0):
                posReinasColocadas.pop()
                contador -= 1
                # Volver
                posXY = setear()
                x = posXY[1]
                y = posXY[0]
                columna = x + 1
                print("Valor seteado para y: ", x)
                print("Valor seteado para x: ", y)
                if (len(posReinasColocadas) > 0):
                    if (posiciones[(len(posiciones)-1)][1] == x):
                        print("La wea 1: ", posiciones)
                        print("La wea 2: ", posReinasColocadas)
                        print("___________________________________________IF DEL IF")
                        posReinasColocadas.clear()
                limpiarMatriz()
                print("Volvemos a la posicion: ", y, ",", x)
                colocarReina(y, x)
                print("-----------------Reina colocada en: ", y, ",", x)
                posReinasColocadas.append([y, x])
                print(matriz)
                continue
            else:
                print("No se encontró solución")
                break
        else:
            print("Primer else...")
            # Hay espacio para la reina
            posXY = setear()
            x = posXY[1]
            y = posXY[0]
            if(len(posReinasColocadas) > 0):
                if (posReinasColocadas[0][1] == x):
                    posReinasColocadas.clear()
            print("-----------------Reina colocada en: ", y, ",", x)
            colocarReina(y, x)
            posReinasColocadas.append([y, x])
            contador += 1
            columna = x + 1
            print(matriz)
            if (contador == numeroReinas):
                print("Solucion encontrada")

buscarSolucionM2()
print(posReinasColocadas)