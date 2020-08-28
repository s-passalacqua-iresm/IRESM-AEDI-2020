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


#print(f'El resultado es: {suma()}')

def que_temperatura_es():
    return '30º'

Método con retorno y con parámetros que cuando recibe dos número enteros, calcule el resultado de dividir el cuadrado del mayor de ellos y el cuadrado del menor de ellos. Si los números son iguales retornar el número 1

