def leerEntero(mensaje):
    """Solicita un entero y repite la petición si la entrada no es válida."""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Entrada no valida. Ingrese un numero entero.")