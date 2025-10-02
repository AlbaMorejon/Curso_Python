import random

def generar_matriz(tamanio):
    """
    Genera una matriz cuadrada de tamaño NxN, donde N es el número ingresado por el usuario.
    Rellena la matriz con números aleatorios entre 0 y 9.
    """
    matriz = [[random.randint(0, 9) for _ in range(tamanio)] for _ in range(tamanio)]
    return matriz

def imprimir_matriz(matriz):
    """
    Imprime la matriz generada en pantalla.
    """
    for fila in matriz:
        print(" ".join(str(elemento) for elemento in fila))

def sumar_filas_columnas(matriz):
    """
    Calcula la suma de los elementos de cada fila y columna de la matriz.
    Retorna dos listas con las sumas de las filas y columnas respectivamente.
    """
    num_filas = len(matriz)
    num_columnas = len(matriz[0])
    sumas_filas = [sum(fila) for fila in matriz]
    sumas_columnas = [sum(matriz[i][j] for i in range(num_filas)) for j in range(num_columnas)]
    return sumas_filas, sumas_columnas

def imprimir_sumas(sumas_filas, sumas_columnas):
    """
    Imprime en pantalla la suma de cada fila y columna.
    """
    print("Suma de cada fila:")
    print(" ".join(str(suma) for suma in sumas_filas))
    print("Suma de cada columna:")
    print([" ".join(str(suma) for suma in sumas_columnas)])








def main():
    try:
        tamanio = int(input("Ingrese el tamaño de la matriz cuadrada (un número entero): "))
        if tamanio <= 0:
            raise ValueError("El tamaño de la matriz debe ser un número entero positivo.")
        
        matriz = generar_matriz(tamanio)
        print("Matriz generada:")
        imprimir_matriz(matriz)

        sumas_filas, sumas_columnas = sumar_filas_columnas(matriz)
        imprimir_sumas(sumas_filas, sumas_columnas)
        
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
