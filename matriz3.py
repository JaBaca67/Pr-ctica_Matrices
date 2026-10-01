from validaciones import leerEntero


def multiplicarMatrices():
    """Lee dos matrices 2x2 y muestra el producto A por B."""
    matrizA = []
    matrizB = []

    print("Ingrese los valores de la matriz A (2x2):")
    for filaIndex in range(2):
        fila = []
        for columnaIndex in range(2):
            valor = leerEntero(f"Ingrese el valor de [{filaIndex + 1}][{columnaIndex + 1}] de A: ")
            fila.append(valor)
        matrizA.append(fila)

    print("Ingrese los valores de la matriz B (2x2):")
    for filaIndex in range(2):
        fila = []
        for columnaIndex in range(2):
            valor = leerEntero(f"Ingrese el valor de [{filaIndex + 1}][{columnaIndex + 1}] de B: ")
            fila.append(valor)
        matrizB.append(fila)

    matrizC = []
    for filaIndex in range(2):
        fila = []
        for columnaIndex in range(2):
            suma = 0
            for productoIndex in range(2):
                suma += matrizA[filaIndex][productoIndex] * matrizB[productoIndex][columnaIndex]
            fila.append(suma)
        matrizC.append(fila)

    print("Matriz C (A x B):")
    for fila in matrizC:
        print(fila)