"""
Vector: coleccion de datos
"""

frutas = ['manzana', 'pera', 'anana']
size = len(frutas)  # Funcion que retorna la cantidad de elementos en el vector

"""
CICLO FOR

"""


def recorrer_vectores_con_for():
    for i in range(0,
                   size):  # recorremos el vector desde la posicion 0 a la ultima / for index en el rango de (inicio, fin sin incluir)
        print(frutas[i])

    print(frutas[1])  # Acceso al elemento en la segunda posicion del vector

    for fruta in frutas:  # por cada fruta en el vector frutas /  por cada item en el vector dado
        print(fruta)  # imprimir el valor fruta


"""
Calcular el promedio de los alumnos de un curso que tiene 10 alumnos
"""


def promedio_de_curso_con_for():
    acum = 0
    for index in range(1, 11):  # for index en el rango de (inicio, fin sin incluir)
        nota = int(input(f'Ingrese nota {index}: '))
        acum = acum + nota

    prom = acum / 10
    print(f'El promedio general del curso es: {prom}')


"""
CICLO WHILE:
Se utiliza cuando no se conoce la condición de corte
Se ejecutra MIENTRAS se cumpla una condición
"""


def ciclo_while():
    temp = 20
    while temp > 0:
        print(f'El agua esta a {temp}ºC, no esta congelada')
        temp = temp - 1

    print(f'El agua llegó a los {temp}ºC, comenzó a congelarse.')


# recorrer_vectores_con_for()
# promedio_de_curso_con_for()
# ciclo_while()
