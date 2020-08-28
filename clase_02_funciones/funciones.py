"""
Parametros o argumentos:
Son los valores que se reciben en una funcion a traves de los parentesis
"""


# Funcion con todos los parametros posicionales requeridos:
def user_info(nombre, edad, ciudad):
    print(f'{nombre} tiene {edad} años y vive en {ciudad}')
    # print('{} tiene {} años y vive en {}'.format(nombre, edad, ciudad))


# Funcion con parametros posicionales opcionales:
def user_info_without_city(nombre, edad, ciudad='Cordoba'):
    print(f'{nombre} tiene {edad} años y vive en {ciudad}')


# user_info('Carlos', 30, 'Carlos Paz')
#
# user_info(edad=30, ciudad='Carlos Paz', nombre='Maria')
#
# user_info(30, 'Carlos Paz', 'Maria')  # Al cambiar la posicion y no especificar el nombre del
#                                       # parametro imprime los valores de forma incorrecta
#
# user_info_without_city('Micaela', 20)


"""
Funciones con retorno:
Son funciones que retornan un valor para ser usado en otra funcion 
"""


def suma():
    a = int(input('Ingrese un numero: '))
    b = int(input('Ingrese otro numero: '))
    return a + b


# print(f'El resultado es: {suma()}')

def que_temperatura_es():
    return '30º'


"""
Método con retorno y con parámetros que cuando recibe dos número enteros, 
calcule el resultado de dividir el cuadrado del mayor de ellos y el cuadrado del menor de ellos. 
Si los números son iguales retornar el número 1
"""
# def division_de_cuadrados(num1, num2):
#     resultado = 1
#     if num1 > num2:
#         resultado = (num1 * num1) / (num2 * num2)
#     elif num2 > num1:
#         resultado = (num2 * num2) / (num1 * num1)
#     else:
#         resultado = 1
#
#     return resultado


def division_de_cuadrados(num1, num2):
    if num1 > num2:
        return (num1 * num1) / (num2 * num2)
    elif num2 > num1:
        return (num2 * num2) / (num1 * num1)
    else:
        return 1


def division_de_cuadrados_x_100(num1, num2):
    r = division_de_cuadrados(num1, num2)
    r_100 = r * 100
    return r_100


def que_temperatura_es_en_celcius(f):
    c = (5 / 9) * (f - 32)
    return c