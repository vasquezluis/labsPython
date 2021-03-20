# Programa para los modelos de Poisson, binomial y normal
# Programa por Luis Vásquez y Benjamyn Recinos
import os
import math

#---------------factorial---------------#
def factorial(n):
    if n < 2:
        return 1
    elif n < 1:
        return 1
    elif n:
        return  n * factorial(n - 1)

#---------------poisson---------------#
def poisson():
    os.system ("cls")

    e = 2.718
    miu = int(input("Ingrese miu: "))
    k = int(input("Ingrese el valor de k: "))
    # factorial de k
    factork = factorial(k)

    #n = int(input("Ingrese la cantidad de ks: "))
    #numk= []
    #for i in range(n):
    #    numk[i] = int(input("k", i+1, ": "))

    #pk1 = ((miu**(numk[0]))*(e**(miu*-1))/(factork))
    #print("El procentaje es:", (round(pk1, 3)) * 100, "\n")

    pk = ((miu**(k))*(e**(miu*-1))/(factork))
    if pk < 0:
        print("Resultado menor a 0")
    else:
        print("El procentaje es:", (round(pk, 3)) * 100, "\n")


    # Fin del modelo
    salir = input("m = ir al menu   r = reiniciar modelo: ")
    if salir == "m":
        menu()
    elif salir == "r":
        poisson()
    else:
        print("Entrada no valida, regresando al menu\n")
        menu()

#---------------binomial---------------#
def binomial():
    os.system ("cls")

    n = int(input("Ingrese numero de ensayos: "))
    x = int(input("Ingrese numero de exitos: "))
    p = float(input("Ingrese l aprobabilidad de exito (decimales): "))
    q = 1-p

    # combinacion
    factor = (factorial(n)/((factorial(x))*(factorial(n-x))))

    # formula
    print("El porcentaje es:", (factor*(p**x)*(q**(n-x)))*100)

    # Fin del modelo
    salir = input("\nm = ir al menu   r = reiniciar modelo: ")
    if salir == "m":
        menu()
    elif salir == "r":
        binomial()
    else:
        print("Entrada no valida, regresando al menu\n")
        menu()

#---------------normal---------------#
def normal():
    os.system ("cls")

    e = 2.718
    x = float(input("Ingrese el promedio: "))
    miu = float(input("Ingrese miu: "))
    sigma = float(input("Ingrese sigma: "))

    # Fórmula
    z = (x - miu)/sigma
    zneg = 1 + z

    if z > 0:
        print("La respuesta es: ", round(z,3))
        parte_decimal, parte_entera = math.modf(z)

        # Separacion
        print(parte_entera)
        print(parte_decimal)
    else:
        print("La respuesta es: ", round(zneg,3))
        parte_decimal, parte_entera = math.modf(zneg)

        #Separacion
        print(parte_entera)
        print(parte_decimal)
    
    
    

    # Fin del modelo
    salir = input("\nm = ir al menu   r = reiniciar modelo: ")
    if salir == "m":
        menu()
    elif salir == "r":
        binomial()
    else:
        print("Entrada no valida, regresando al menu\n")
        menu()


#---------------menu---------------#
def menu():
    os.system ("cls")
    print("Programa para modelos\n")
    print("1. Poisson   2. Binomial     3. Normal\n")
    seleccion = int(input("Selecciona un modelo: "))
    if seleccion == 1:
        poisson()
    elif seleccion == 2:
        binomial()
    elif seleccion == 3:
        normal()
    else: 
        menu()
    

#---------------Inicio---------------#
menu()
