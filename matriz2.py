
from validaciones import leerEntero


def mostrarMatriz():
    """Solicita los valores de una matriz 2x2 y la muestra por filas."""
    matriz = []
    for filaIndex in range(2):
        fila = []
        for columnaIndex in range(2):
            valor = leerEntero(f"Ingrese el valor de [{filaIndex + 1}][{columnaIndex + 1}] de la matriz: ")
            fila.append(valor)
        matriz.append(fila)

    print("Matriz ingresada:")
    for fila in matriz:
        print(fila)