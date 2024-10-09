def ejercicio11():
    numero = int(input("Introduce un número: "))
    if numero < 2:
        print("No es primo")
        return

    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            print("No es primo")
            return

    print("Es primo")

ejercicio11()