"""
Diccionarios:
    Contenido: son pares de key/value
    Mutables: pueden modificarse
    Order: puede mantener un orden de entrada
    Sintaxis: llaves que contienen una key, :, un valor u esos pares de key/value son separados por coma
"""

años = {'Laila': 1974, 'Matias': 1997}

cosas = {'comida': 15, 'energia': 100, 'enemigos':3}

e = cosas.get('energia')  # Obtener el valor segun la key
#e = cosas.get('nada', 'No existe') # parametro opcional despues de la coma poner el valor que queres que te retorne si no encuentra el elemento
print(e)

print(cosas.items()) # Imprime todos los elementos del diccionario

print(cosas.keys()) # Imprime las keys del diccionario

# cosas.popitem() # Remueve el ultimo elemento del diccionario

print(cosas.items())

new_items = {'rocas': 4, 'flechas': 5}

cosas.update(new_items)  # El metodo update actualiza los valores segun la key, si la key no existe agrega el elemento
print(cosas.items())

up_new = {'comida': 3, 'redes': 2}

cosas.update(up_new)
print(cosas.items())


cosas.setdefault('red', 100) # agrega un nuevo elemento al diccionario
print(cosas.items())

cosas['comida'] = 100 # Actualiza el valor de una key en el diccionario, si no existe la agrega
print(cosas.items())

cosas['arcos'] = 100
print(cosas.items())

comida = cosas['comida'] # Obtiene el valor segun la key. Si la key no existe devuelve error!
print(f'la cantidad de comida es: {comida}')

comida = cosas.get('comida')
print(f'la cantidad de comida es: {comida}')

