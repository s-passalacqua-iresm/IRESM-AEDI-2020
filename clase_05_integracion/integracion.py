"""
Una librería de la ciudad de Carlos Paz requiere de un programa que permita cargar los montos de todas las ventas
realizadas. Para ello el programa debe permitir guardar ese valor en una lista.
Se debe generar un menú que permita realizar las siguientes operaciones:

Agregar el monto de una venta.
Mostrar todos los datos cargados en la lista.
Mostrar la venta más baja.
Mostrar la ganancia total (Suma de todas las ventas).
Calcular el promedio de Ventas.

Cada opción (a excepcion de la primera) debe llamar a una función que se encargue de hacer el calculo correspondiente
recibiendo la lista por parametro y retornando el valor correspondiente.
"""
from clase_05_integracion import funciones_para_ventas

def opciones_del_menu():
    print("Ingrese 1 para cargar una venta\n"
          "Ingrese 2 para mostrar la lista de las ventas cargadas\n"
          "Ingrese 3 para mostrar la venta mas baja\n"
          "Ingrese 4 para mostrar la ganancia total\n")

    return int(input("Ingrese una opcion: "))

def menu():
    lista_ventas = []

    opcion = opciones_del_menu()

    while opcion != 0:
        if opcion == 1:
            venta = float(input("Ingrese el monto de la venta: "))
            lista_ventas.append(venta)
        elif opcion == 2:
            funciones_para_ventas.imprimir_lista(lista_ventas)
        elif opcion == 3:
            print(f'La menor venta es: {funciones_para_ventas.venta_minima(lista_ventas)}')
        elif opcion == 4:
            r = funciones_para_ventas.venta_total(lista_ventas)
            print(f'La ganancia total es: {r}')
        elif opcion == 5:
            r = funciones_para_ventas.promedio_ventas(lista_ventas)
            print(f'El promedio de las ventas es: {r}')
        else:
            print("Opción incorrecta!")

        opcion = opciones_del_menu()


menu()