# Este es un comentario simple

"""
Este es un comentario donde se pueden escribir varias lineas
Normalmente es usado para docstrings
o para especificar indicaciones o dodigo complejo
"""

# print('Hola Mundo') #Para mostrar mensajes por pantalla
# input('Ingrese un numero: ') #Ingresar datos por teclado con las indicaciones entre comillas

# Convención de nombres


"""
Variables numericas:
int -> numeros enteros
float -> numeros decimales
"""
car = 10
CAR = 20
_car = 30
"""
str -> Variables String, es decir texto
"""
texto = 'esta es una variable tipo str'
texto_uno = '10'
"""
Bool -> boolean (True o False)
"""

suma = int(texto_uno) + car


def calcular_nota():
    nombre = input('Ingrese el nombre del alumno: ')
    num1 = float(input('Ingrese primer nota: '))
    num2 = int(input('Ingrese segunda nota: '))

    prom = (num1 + num2) / 2
    print("El promedio de " + nombre + " es: " + str(prom))
    print("El promedio de {} es: {}".format(nombre, prom))
    print(f"El promedio de {nombre} es: {prom}")

    if prom >= 7:
        print('El alumno esta promocionado')
    elif prom >= 4:
        print('El alumno esta regular')
    else:
        print('El alumno esta libre')

calcular_nota()
