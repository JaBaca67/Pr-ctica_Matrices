
matriz = [[1,2],[3,4]]

for fila in matriz:
    print(fila)

#Escalar
k = 5

matrizB = []
for i in range(len(matriz)):
    matrizB.append([])
    for j in range(len(matriz)):
        matrizB[i].append(k * matriz[i][j]) 

print("="*67)
print(f"Escalar de la matriz A por k = {k} ")
for fila in matrizB:
    print(fila)





