"""
Clases
Las clases pueden escribirse en un unico archivo .py o pueden agruparse en uno mismo, siempre y cuando compartan
funcionalidades simaleres

def __init__(self):  Para crear instancias de una clase con parametros especificos, es el constructor del objeto
                     Asignamos los valores a los atributos
                     No es requerido (puede estar o no), pero se usa para asignar el estado por defecto a los objetos cuando se crean
                     Es el primer metodo de la clase

self: Representa a la instancia de la clase, lo usamos para hacer referencia a las variables y metodos de la clase,
de esta manera podemos compartir informacion eficiente y facilmente dentro de la clase

"""


class Persona:

    def __init__(self, nombre, apellido, salud, estado_de_amistad):
        """
        Inicializamos los atributos que seran usados en los metodos de esta clase y por los objetos que fueran creados
        a partir de ella
        """
        self.nombre = nombre
        self.apellido = apellido
        self.salud = salud
        self.estado_de_amistad = estado_de_amistad

    def presentarse(self):
        """
        Una persona se presenta por nombre y apellido
        """
        print(f'Hola, mi nombre es: {self.nombre} {self.apellido}')

    def estado_salud(self):
        """
        Una persona puede cambiar su estado de salud, el metodo muestre por pantalla el estado de salud segun el valor
        asignado
        """
        if self.salud == 100:
            print(f'{self.nombre} esta joya')
        elif self.salud >= 76:
            print(f'Hoy {self.nombre} esta con cansancio')
        elif self.salud >= 51:
            print(f'{self.nombre} debe ir al medico')
        else:
            print(f'{self.nombre}  tiene el bicho')


