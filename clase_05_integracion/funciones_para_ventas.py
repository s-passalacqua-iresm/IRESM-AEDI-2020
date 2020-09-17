"""
Mostrar todos los datos cargados en la lista.
Mostrar la venta más baja.
Mostrar la ganancia total (Suma de todas las ventas).
Calcular el promedio de Ventas.
"""

def imprimir_lista(lista):
    print("El listado de ventas es: ")
    print(lista)
    for i in range(0, len(lista)):
        print(f"Venta Nº {i}: {lista[i]}")


def venta_total(lista):
    acum = 0
    for item in lista:
        acum = acum + item
    return acum


def venta_minima(lista):
    menor = lista [0]
    for item in lista:
        if item < menor:
            menor = item
    return menor


def promedio_ventas(lista):
    return venta_total(lista)/len(lista)