def mostrarIdentidadColoreada():
    """Muestra una matriz identidad 3x3 con la diagonal en azul."""
    import colorama

    colorama.init(autoreset=True)
    matrizIdentidad = []

    for filaIndex in range(3):
        fila = []
        for columnaIndex in range(3):
            fila.append(1 if filaIndex == columnaIndex else 0)
        matrizIdentidad.append(fila)

    for fila in matrizIdentidad:
        for elemento in fila:
            if elemento == 1:
                print(colorama.Back.BLUE + str(elemento) + colorama.Style.RESET_ALL, end=" ")
            else:
                print(elemento, end=" ")
        print()

