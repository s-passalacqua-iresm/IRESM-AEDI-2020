from IRESM_AEDI_2020.practica2 import funciones

print("                               INGRESE LA OPCION QUE DESEA           ")
print("(1) Algoritmo que lea un número entero y verifique si es mayor a 10. ")
print("(2) Algoritmo que reciba 3 números, y determine si la suma del primero y el segundo es igual al tercero. ")
print("(3) Algoritmo recibe dos número enteros Y calcule el resultado de dividir el cuadrado del mayor de ellos y el cuadrado del menor de ellos. ")
print("(4) Algoritmo que convierta temperaturas de Fahrenheit a Celcius. ")

opcion=int(input("------------> "))

if opcion == 1:

    funciones.num_mayor_10()

elif opcion == 2:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    num3 = float(input("Ingrese el tercer número: "))

    funciones.suma_prim_igual_ter(num1, num2, num3)

elif opcion == 3:
    a = int(input("Ingrese el primer numero entero: "))
    b = int(input("Ingrese el segundo numero entero: "))

    funciones.dos_num_enteros(a, b)

elif opcion == 4:

    funciones.celcius_to_fal()

else print("Numero incorrecto")






















