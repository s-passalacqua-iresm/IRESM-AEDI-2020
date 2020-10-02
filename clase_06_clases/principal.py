from clase_06_clases.clases import Persona

maria = Persona(nombre='Maria', apellido='Gonzalez', salud=100, estado_de_amistad=True)
martin = Persona('Martin', 'Paez', 88, False)
leo = Persona('Leo', 'Williams', 72, True)
luis = Persona('Luis', 'Williams', 40, True)

n = input("Ingresa el nombre: ")
apellido = input('Ingresa el apellido: ')
salud = int(input('Ingresa el porcentaje de salud: '))
amistad = bool(input('Es amigo: '))

per = Persona(n, apellido, salud, amistad)

personas = [maria, martin, leo, luis, per]

for p in personas:
    p.presentarse()
    print(f'¿Como esta {p.nombre} hoy?')
    p.estado_salud()
    print(f'¿{p.nombre} es amig@ mio?: {p.estado_de_amistad}')



