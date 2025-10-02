#importamos la biblioteca random
import random

# Generamos una matriz con numeros aleatorios entre 0 y 9
def nueva_matriz(n):
    matriz = [[random.randint(0, 9) for _ in range(n)] for _ in range(n)]
    print("Matriz generada: ")
    for fila in matriz:
        print(fila)
    return matriz

# Calculamos la suma de cada fila y cada columna
def calcular_suma(matriz):
    suma_fila = [sum(fila) for fila in matriz]
    suma_columna = [sum(columna) for columna in zip(*matriz)]

    for i in range(len(suma_fila)):
        print(f"Suma fila {i + 1}= ", suma_fila[i])
    for j in range(len(suma_columna)):
        print(f"Suma columna {j + 1}= ", suma_columna[j])
    return suma_fila, suma_columna

# Excepciones
try:
    # El usuario nos da el tamaño de la matriz.
    size_input = input("Introduce el tamaño de la matriz: ")
    n = int(size_input)

    if n <= 0:
        # No queremos una valor negativo o igual a 0.
        raise ValueError("Invalid input. Please enter a positive integer for the size of the matriz.")

    # Generamos la matriz
    matriz = nueva_matriz(n)

    # Calculate the sums
    suma_fila, suma_columna = calcular_suma(matriz)

# Errores
except ValueError:
    try:
        # Muestra este ValueError cuando se introduce un numero menor a 0.
        raise TypeError("Valor incorrecto. Introduzca un numero entero.")
    except TypeError:
        # Muestra este TypeError cuando se introduce un numero no entero.
        print(f"Error: Valor incorrecto. El número introducido '{size_input}' no es un entero valido.")
except ZeroDivisionError:
    # Muestra este ZeroDivisionError cuando se introduce el numero 0.
    print("Error: El numero introducido es 0. Introduzca un numero diferente.")
