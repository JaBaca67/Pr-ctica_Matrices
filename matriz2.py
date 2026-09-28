
matriz = []
#Pedir los datos de matriz A
for i in range(2):   
    matriz.append([])
    for j in range(2):
        matriz[i].append(int(input(f"Ingresa el valor de la posición [{i + 1}][{j + 1}] de la matriz A: ")))


print(matriz)