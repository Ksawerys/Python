def ejercicio12():
    año = int(input("Introduce un año: "))
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        print("El año es bisiesto")
    else:
        print("El año no es bisiesto")

ejercicio12()