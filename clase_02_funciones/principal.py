from clase_02_funciones import funciones


def menu():
    funciones.user_info('Maria', 30, 'Carlos Paz')

    temp = funciones.que_temperatura_es()
    print(f'la temperatura es: {temp}')

menu()
