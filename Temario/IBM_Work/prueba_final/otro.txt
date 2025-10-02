import random

def generar_matriz(n):
    matriz = []
    for _ in range(n):
        fila = []
        for _ in range(n):
            fila.append(random.randint(0, 5))
        matriz.append(fila)
    return matriz

def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

def calcular_suma_filas(matriz):
    suma_filas = []
    for fila in matriz:
        suma_filas.append(sum(fila))
    return suma_filas

def calcular_suma_columnas(matriz):
    suma_columnas = []
    for j in range(len(matriz[0])):
        suma_columna = 0
        for i in range(len(matriz)):
            suma_columna += matriz[i][j]
        suma_columnas.append(suma_columna)
    return suma_columnas

def imprimir_suma_filas(suma_filas):
    print("Suma de cada fila:")
    for suma in suma_filas:
        print(suma)

def imprimir_suma_columnas(suma_columnas):
    print("Suma de cada columna:")
    for suma in suma_columnas:
        print(suma)

# Pedir al usuario el tamaño de la matriz
n = int(input("Ingrese el tamaño de la matriz: "))

# Generar la matriz
matriz = generar_matriz(n)

# Imprimir la matriz generada
print("Matriz generada:")
imprimir_matriz(matriz)

# Calcular la suma de los elementos de cada fila y columna
suma_filas = calcular_suma_filas(matriz)
suma_columnas = calcular_suma_columnas(matriz)

# Imprimir la suma de cada fila y columna
imprimir_suma_filas(suma_filas)
imprimir_suma_columnas(suma_columnas)