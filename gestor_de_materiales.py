
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

while opcion != 4:
    print("\n===== GESTOR DE MATERIALES =====")
    print("1. Consultar inventario")
    print("2. Retirar producto")
    print("3. Reponer producto")
    print("4. Salir")

    opcion = leer_entero_rango("Selecciona una opción (1-4): ", 1, 4)

    if opcion == 1:
        print("\n===== INVENTARIO ACTUAL =====")

        for posicion in range(len(inventario)):
            producto = posicion + 1
            cantidad = inventario[posicion]
            clasificacion = consultar_existencia(inventario, posicion)

            print(
                f"Producto {producto}: "
                f"{cantidad} unidades - {clasificacion}"
            )

    elif opcion == 2:
        producto = leer_entero_rango(
            "¿Qué producto deseas retirar? (1-3): ", 1, 3
        )

        cantidad = leer_entero_rango(
            "¿Cuántas unidades deseas retirar? (1-20): ", 1, 20
        )

        posicion = producto - 1
        mensaje = retirar_articulo(inventario, posicion, cantidad)
        print(mensaje)

    elif opcion == 3:
        producto = leer_entero_rango(
            "¿Qué producto deseas reponer? (1-3): ", 1, 3
        )

        cantidad = leer_entero_rango(
            "¿Cuántas unidades deseas reponer? (1-20): ", 1, 20
        )

        posicion = producto - 1
        mensaje = reponer_existencia(inventario, posicion, cantidad)
        print(mensaje)

    elif opcion == 4:
        print("Programa finalizado. ¡Hasta luego!")


