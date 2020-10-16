from clase_07_clases_busqueda_json.clases import Empleado, GestionarEmpleados


def opciones_menu():
    print('---------------------------------------------------------------------------------------\n'
          'Ingrese 1 para cargar un empleado\n'
          'Ingrese 2 para mostrar la lista de empleados\n'
          'Ingrese 3 para buscar un empleado por legajo y mostrar todos sus datos\n'
          'Ingrese 4 para buscar un empleado por nombre y asignarle horas trabajadas\n'
          'Ingrese 5 para conocer el porcentaje de empleados con un sueldo menor a 30.000 pesos\n'
          'Ingrese 0 para salir\n')

    return int(input('Ingrese opción: '))


def menu():
    gestor_empleados = GestionarEmpleados()
    empleados = []

    opcion = opciones_menu()

    while opcion != 0:

        if opcion == 1:
            nombre = input('Ingrese nombre:')
            apellido = input('Ingrese apellido:')
            dni = input('Ingrese DNI:')
            legajo = int(input('Ingrese legajo:'))
            puesto = input('Ingrese Puesto:')
            salario_por_hora = float(input('Ingrese salario por hora:'))

            empleado = Empleado(nombre=nombre, apellido=apellido, dni=dni, legajo=legajo, puesto=puesto,
                                salario_por_hora=salario_por_hora)
            empleados.append(empleado)

        elif opcion == 2:
            gestor_empleados.imprimir_lista(empleados)

        elif opcion == 3:
            gestor_empleados.buscar_empleado_por_legajo(empleados)

        elif opcion == 4:
            gestor_empleados.asignar_horas(empleados)

        elif opcion == 5:
            gestor_empleados.porcentaje_de_sueldo_menor(empleados)

        opcion = opciones_menu()


menu()


