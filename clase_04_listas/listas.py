"""
Listas:

Coleccion de datos
Pueden contener distintos tipos de datos
Pueden conter otras colecciones (listas, diccionarios, tuplas) como elemento dentro de la lista
Es mutable: se pueden agregar, remover o cambiar items
Pueden mantener un orden, por lo que se puede acceder a los elementos mediante un indice
"""

frutas = ['manzana', 'peras', 'durazno']
años = [3, '1998', 2.5, 234, 943]
numeros = [3, 1998, 2.5, 234, 943]

"""
print(frutas, años)

frutas.append('naranja') # metodo para agregar elementos en la lista

frutas.insert(2, 'anana') # metodo para agregar un elemento en la posicion indicada por parametro

print(frutas)

frutas.extend(años) # nos permite unir dos listas

print(frutas)

frutas.remove('naranja') # Remueve un elemento de la lista por coincidencia exacta, si no exite imprime error

print(frutas)

frutas.pop(0)  # Elimina el elemento en el indice indicado (0 = primer elemento), (-1 = ultimo elemento)
frutas.pop(-1)

print(frutas)


# Para ordenar una lista se utiliza el metodo sort(), y funciona solo con elementos del mismos tipo
print('----------------------------------------')
print(frutas)
frutas.sort()
print(frutas)
print('----------------------------------------')
print(numeros)
numeros.sort()
print(numeros)
print('----------------------------------------')
#print(años)
#print(años.sort())
"""

# Como saber si un elemento es miembro de una lista
print(frutas)
frutas.append('manzana')
print(frutas)

print('manzana' in frutas)   # True o False segun se encuentre o no el elemento en la lista
print('manzanas' in frutas)

print(frutas.count('manzana'))   # Cuenta la cantidad de veces que se encuentra el elemento en la lista
print(frutas.count('manzanas'))

print(frutas.index('manzana'))  # Devuelve el indice en el que se encuentra el elemento con la primera coincidencia, si no se encuentra falla

corona = ['negative', 'negative', 'negative', 'negative']

todos_los_casos_son_negativos = all(c == 'negative' for c in corona) # all sirve para conocer si TODOS los elementos de una coleccion cumplen un determiando criterio
hay_algun_caso_negativo = any(c == 'negative' for c in corona) # any sirve para conocer si ALGUNO de los elementos de una coleccion cumplen un determiando criterio

print(todos_los_casos_son_negativos)
print(hay_algun_caso_negativo)