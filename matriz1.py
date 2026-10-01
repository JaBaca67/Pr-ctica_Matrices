
from validaciones import leerEntero


def multiplicarPorEscalar():
    """Lee una matriz 2x2 y multiplica sus elementos por un escalar."""
    matriz = []
    for filaIndex in range(2):
        fila = []
        for columnaIndex in range(2):
            valor = leerEntero(f"Ingrese el valor de [{filaIndex + 1}][{columnaIndex + 1}] de la matriz: ")
            fila.append(valor)
        matriz.append(fila)

    escalar = leerEntero("Ingrese el escalar: ")
    matrizResultado = []
    for fila in matriz:
        matrizResultado.append([escalar * valor for valor in fila])

    print("Matriz original:")
    for fila in matriz:
        print(fila)

    print(f"Matriz multiplicada por {escalar}:")
    for fila in matrizResultado:
        print(fila)





