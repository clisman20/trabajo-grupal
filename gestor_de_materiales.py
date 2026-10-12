def consultar_existencia(mi_lista: list, posicion: int):
    cantidad = mi_lista[posicion]

    if cantidad == 0:
        resultado = "Agotado"
    elif cantidad <= 5:
        resultado = "Existencia baja"
    else:
        resultado = "Existencia suficiente"

    return resultado


def retirar_articulo(mi_lista: list, posicion: int, cantidad: int):
    existencia = mi_lista[posicion]

    if existencia < cantidad:
        resultado = "No hay suficientes unidades disponibles"
    else:
        mi_lista[posicion] = existencia - cantidad
        resultado = "Producto retirado correctamente"

    return resultado


def reponer_existencia(mi_lista: list, posicion: int, cantidad: int):
    mi_lista[posicion] = mi_lista[posicion] + cantidad
    resultado = "Producto repuesto correctamente"

    return resultado


# EDITAR 1: Sustituye estos ceros por las cantidades iniciales
# que aparecen en tu enunciado, en el orden de los productos 1, 2 y 3.
inventario = [0, 0, 0]


# Función para validar que el usuario introduzca un entero
# dentro del rango permitido.
def leer_entero_rango(mensaje: str, minimo: int, maximo: int):
    while True:
        try:
            numero = int(input(mensaje))

            if minimo <= numero <= maximo:
                return numero
            else:
                print(f"Error: introduce un número entre {minimo} y {maximo}.")

        except ValueError:
            print("Error: debes introducir un número entero.")


# Menú principal
opcion = 0

