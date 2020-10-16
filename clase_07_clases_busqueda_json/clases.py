

class Empleado:

    def __init__(self, nombre, apellido, dni, legajo, puesto, salario_por_hora):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.legajo = legajo
        self.puesto = puesto
        self.salario_por_hora = salario_por_hora
        self.cantidad_hs_trabajadas = 0

    def mostrar_datos(self):
        print('------------------------------------')
        print(f'Nombre: {self.nombre}')
        print(f'Apellido: {self.apellido}')
        print(f'DNI: {self.dni}')
        print(f'Legajo: {self.legajo}')
        print(f'Puesto: {self.puesto}')
        print(f'Salario por hora: {self.salario_por_hora}')
        print(f'Cantidad de horas trabajadas: {self.cantidad_hs_trabajadas}')
        print(f'Sueldo calculado: {self.cantidad_hs_trabajadas * self.salario_por_hora}')


    def asignar_cantidad_de_horas(self, cantidad_hs):
        self.cantidad_hs_trabajadas = cantidad_hs

    def calcular_sueldo(self):
        return self.cantidad_hs_trabajadas * self.salario_por_hora


class GestionarEmpleados:

    def imprimir_lista(self, lista):
        for item in lista:
            item.mostrar_datos()

    def buscar_empleado_por_legajo(self, lista):
        legajo = int(input('Ingrese legajo a buscar: '))
        bandera = False
        for item in lista:
            item: Empleado
            if legajo == item.legajo:
                print('------------------------------------')
                print('Empleado encontrado ')
                item.mostrar_datos()
                bandera = True
                break

        if bandera == False:
            print('------------------------------------')
            print('Empleado NO encontrado')
            print('------------------------------------')

    def asignar_horas(self, lista):
        nombre = input('Ingrese el nombre del empleado al que le quiere cargar las horas: ')
        bandera = False
        for item in lista:
            item: Empleado
            if nombre == item.nombre:
                cant_hs = int(input(f'Ingrese la cantidad de horas que trabajo {item.nombre}: '))
                item.asignar_cantidad_de_horas(cant_hs)
                bandera = True
                break

        if bandera == False:
            print('------------------------------------')
            print('Empleado NO encontrado, no se pueden asignar las horas')
            print('------------------------------------')

    def porcentaje_de_sueldo_menor(self, lista):
        contador = 0
        size = len(lista)
        for item in lista:
            item: Empleado
            sueldo = item.calcular_sueldo()
            if sueldo < 30000:
                contador = contador + 1

        print(f'El porcentaje de empleados que cobran menos de $30.000 es de {contador/size*100} %')