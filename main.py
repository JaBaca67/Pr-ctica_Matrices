from matriz import sumarMatrices
from matriz1 import multiplicarPorEscalar
from matriz2 import mostrarMatriz
from matriz3 import multiplicarMatrices
from matriz4 import mostrarIdentidadColoreada
from menu import mostrarMenu
from validaciones import leerEntero


def main():
	while True:
		mostrarMenu()
		opcion = leerEntero("Seleccione una opcion: ")

		if opcion == 1:
			sumarMatrices()
		elif opcion == 2:
			multiplicarPorEscalar()
		elif opcion == 3:
			multiplicarMatrices()
		elif opcion == 4:
			mostrarMatriz()
		elif opcion == 5:
			mostrarIdentidadColoreada()
		elif opcion == 6:
			print("Programa finalizado.")
			break
		else:
			print("Opcion no valida. Intente de nuevo.")


if __name__ == "__main__":
	main()
