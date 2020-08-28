from clase_02_funciones import funciones


def menu():
    funciones.user_info('Maria', 30, 'Carlos Paz')

    temp = funciones.que_temperatura_es()
    print(f'la temperatura es: {temp}')

    resultado = funciones.division_de_cuadrados(2, 4)
    print(f'La division de los cuadrados es: {resultado}')

    res_100 = funciones.division_de_cuadrados_x_100(2, 4)#resultado * 100
    print(f'La division de los cuadrados multiplicada por 100 es: {res_100}')

    celcius = funciones.que_temperatura_es_en_celcius(32)
    print(f'La temperatura en celcius es: {celcius}º')

menu()
