from validaciones import leerEntero


def sumarMatrices():
    """Lee dos matrices 3x3 y muestra su suma."""
    matrizA = []
    matrizB = []

    print("Ingrese los valores de la matriz A (3x3):")
    for filaIndex in range(3):
        fila = []
        for columnaIndex in range(3):
            valor = leerEntero(f"Ingrese el valor de [{filaIndex + 1}][{columnaIndex + 1}] de A: ")
            fila.append(valor)
        matrizA.append(fila)

    print("Ingrese los valores de la matriz B (3x3):")
    for filaIndex in range(3):
        fila = []
        for columnaIndex in range(3):
            valor = leerEntero(f"Ingrese el valor de [{filaIndex + 1}][{columnaIndex + 1}] de B: ")
            fila.append(valor)
        matrizB.append(fila)

    sumaMatrices = []
    for filaIndex in range(3):
        fila = []
        for columnaIndex in range(3):
            fila.append(matrizA[filaIndex][columnaIndex] + matrizB[filaIndex][columnaIndex])
        sumaMatrices.append(fila)

    print("Matriz A:")
    for fila in matrizA:
        print(fila)

    print("Matriz B:")
    for fila in matrizB:
        print(fila)

    print("Suma de las matrices A y B:")
    for fila in sumaMatrices:
        print(fila)