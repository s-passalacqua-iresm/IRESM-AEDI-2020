
def num_mayor_10():

    num1 = int(input("Ingrese un numero "))

    if num1 > 10:
        print(f"El numero es {num1}")
    elif num1 == 10:
        print("El numero es igual a 10")

    else:
        print("Su numero es menor a 10")





def suma_prim_igual_ter(num1, num2, num3):

    suma = num1 + num2

    if suma == num3:
        print("La suma es igual al tercero")

    else:
        print("La suma es distinta al tercero")





def dos_num_enteros(a, b):

    if a > b:
        CuadradoPrimero = a ^ 2
        CuadradoSegundo = b ^ 2
    elif a == b:

        z=str("1")
        return z
    else:
        CuadradoPrimero = b ^ 2
        CuadradoSegundo = a ^ 2

    Division = CuadradoPrimero / CuadradoSegundo

    return Division







def celcius_to_fal():
    var1 = float(input("Ingrese la tamperatura que desea convertir a Celcius: "))
    Celcius = (5 / 9) * (var1 - 32)

    return Celcius















