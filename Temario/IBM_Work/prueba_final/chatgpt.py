import random

def generar_matriz(N):
    """
    Genera una matriz cuadrada de tamaño NxN y la llena con números aleatorios entre 0 y 9.
    """
    matriz = []
    for _ in range(N):
        fila = []
        for _ in range(N):
            # Generar número aleatorio entre 0 y 9
            numero = random.randint(0, 9)
            fila.append(numero)
        matriz.append(fila)
    return matriz

def sumar_filas_columnas(matriz):
    """
    Calcula la suma de los elementos de cada fila y columna de la matriz.
    Retorna dos listas con las sumas de las filas y columnas respectivamente.
    """
    sumas_filas = []
    sumas_columnas = []

    for fila in matriz:
        suma_fila = sum(fila)
        sumas_filas.append(suma_fila)

    for i in range(len(matriz)):
        suma_columna = sum(fila[i] for fila in matriz)
        sumas_columnas.append(suma_columna)

    return sumas_filas, sumas_columnas

def imprimir_matriz(matriz):
    """
    Imprime la matriz en pantalla.
    """
    for fila in matriz:
        print(fila)

def imprimir_sumas(sumas_filas, sumas_columnas):
    """
    Imprime las sumas de las filas y columnas en pantalla.
    """
    print("Sumas de las filas:")
    for suma in sumas_filas:
        print(suma)

    print("Sumas de las columnas:")
    for suma in sumas_columnas:
        print(suma)

# Pedir al usuario el tamaño de la matriz
try:
    N = int(input("Ingrese el tamaño de la matriz cuadrada: "))
    if N <= 0:
        raise ValueError
except ValueError:
    print("Error: El tamaño debe ser un número entero mayor a cero.")
    
    
else:
    # Generar la matriz
    matriz = generar_matriz(N)

    # Imprimir la matriz generada
    print("Matriz generada:")
    imprimir_matriz(matriz)

    # Calcular la suma de las filas y columnas
    sumas_filas, sumas_columnas = sumar_filas_columnas(matriz)

    # Imprimir las sumas de las filas y columnas
    imprimir_sumas(sumas_filas, sumas_columnas)
