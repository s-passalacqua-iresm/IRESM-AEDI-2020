"""
Nombre de la función: ejercicio_1_for_en_vector
En esta función agregar el vector:
nombres = ['Lucas','Franco','Luciano','Malena','Jonatan','Luciano','Rodrigo','Maria Sol','Enzo','Milena']

Recorra el vector e imprima los elementos utilizando el ciclo for sin índices (sin la función range)

"""

def ejercicio_1_for_en_vector():

    nombres = ['Lucas', 'Franco', 'Luciano', 'Malena', 'Jonatan', 'Luciano', 'Rodrigo', 'Maria Sol', 'Enzo', 'Milena']

    for nomb in nombres:
        print(nomb)


def ejercicio_2_for_en_vector():

    nombres = ['Lucas', 'Franco', 'Luciano', 'Malena', 'Jonatan', 'Luciano', 'Rodrigo', 'Maria Sol', 'Enzo', 'Milena']

    size = len(nombres)
    for i in range(0, size):
        print(f'El nombre en la posicion {i} es: {nombres[i]}')


def acceder_a_vector():

    numeros = [1, 3, 343, 213, 94]

    a = numeros[0]
    b = numeros[1]
    c = numeros[2]
    d = numeros[3]
    e = numeros[4]

    suma = a + b + c + d + e

    print(suma)

    size = len(numeros)
    acum = 0
    for i in range(0, size):
        acum = acum + numeros[i]

    print(f'La suma es: {acum}')


def cargar_vector():

    notas = []

    size = int(input('Cuantas notas desea ingresar: '))

    for i in range(0, size):
        nota = int(input('Ingrese nota: '))
        notas.append(nota)

    print(notas)


"""
Nombre de la función: ejercicio_4_while
Realice una funcion que mientras la nota ingresada sea distinta de 0 le solicite al profesor el ingreso de otra nota, 
una vez que el profesor ingrese la nota 0 deberá imprimir un mensaje con el promedio de todas las notas ingresadas
"""

def while_notas():

    nota = int(input('Ingrese una nota, presione 0 para finalizar: '))
    acum = 0
    contar = 0

    while nota != 0:
        acum = acum + nota
        contar = contar + 1
        nota = int(input('Ingrese una nota, presione 0 para finalizar: '))

    if contar != 0:
        print(f'El promedio del curso es: {acum/contar}')
    else:
        print('No ha sido ingresada ninguna nota')
