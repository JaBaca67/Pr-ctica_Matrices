#Suma de matrices

"""Leer 2 matrices de 3x3 y sumar en una sola matriz"""

matrizA = []
matrizB = []
sumaMatrizAB = []

#Pedir los datos de la matrizA

for i in range(3):
    matrizA.append([])
    for j in range(3):
        matrizA[i].append(int(input(f"IngreseA el valor de la posición [{i+1}] [{j+1}] de la matriz A: ")))

print("="*13)
print("Matriz A:")
for fila in matrizA:
    print(fila)
print("="*13)

for i in range(3):
    matrizB.append([])
    for j in range(3):
        matrizB[i].append(int(input(f"Ingrese el valor de la posición [{i+1}] [{j+1}] de la matriz B: ")))


print("Matriz B:")
for fila in matrizB:
    print(fila)
print("="*13)

#Sumar las matrices A y B
for i in range(3):
    sumaMatrizAB.append([])
    for j in range(3):
        sumaMatrizAB[i].append(matrizA[i][j] + matrizB[i][j])

print("="*67)
print("Suma de la matriz A y B fila por fila: ")

for fila in sumaMatrizAB:
    print(fila)