#importamos la biblioteca random
import random

# Generamos una matriz con numeros aleatorios entre 0 y 9
def generar_matriz_aleatoria(n):
    matriz = [[random.randint(0, 9) for _ in range(n)] for _ in range(n)]
    return matriz

# Calculamos la suma de cada fila y cada columna
def calcular_suma_filas_columnas(matriz):
    suma_filas = [sum(fila) for fila in matriz]
    suma_columnas = [sum(columna) for columna in zip(*matriz)]
    return suma_filas, suma_columnas

# Se solicita el tamaño de la matriz al usuario y se convierte a formato int
try:
    tamaño_input = input("Introduce el tamaño de la matriz: ")
    n = int(tamaño_input)

# El numero no debe ser menos a cero, ni mayor a 100, para no tener problemas
    if n <= 0 or n > 100:
        raise ValueError("Valor incorrecto. Por favor, introduce un numero entero positivo, entre 0 y 100 para el tamaño de la matriz.")

# Si la entrada del usuario es valida, se genera la matriz
    matriz = generar_matriz_aleatoria(n)

    print(">> Matriz generada:")
    for fila in matriz:
        print(fila)

    suma_filas, suma_columnas = calcular_suma_filas_columnas(matriz)
    
# Se muestra el resultado de las sumas por filas
    print(">> Suma de las filas: ")
    for i, suma_fila in enumerate(suma_filas):
        print(f"Suma fila {i + 1} = {suma_fila}")
    
# Se muestra el resultado de las sumas por columnas
    print(">> Suma de las columnas: ")
    for j, suma_columna in enumerate(suma_columnas):
        print(f"Suma columna {j + 1} = {suma_columna}")

# Se muestran ambos resultados en listas
    resultados_filas= []
    for i, suma_fila in enumerate(suma_filas):
        resultados_filas.append(suma_fila)

    resultados_columnas= []
    for j, suma_columna in enumerate(suma_columnas):
        resultados_columnas.append(suma_columna)

# Se muestra ambos resultados juntos y en tuplas
    print(">> Resultados:")
    print(f"Suma filas: {resultados_filas}")
    print(f"Suma columnas: {resultados_columnas}")

# Se manejan los posibles errores
except ValueError as ve:
    print(f"Error: {ve}. Por favor, introduce un valor válido para el tamaño de la matriz.")
except Exception as e:
    print(f"Error inesperado: {e}")
    