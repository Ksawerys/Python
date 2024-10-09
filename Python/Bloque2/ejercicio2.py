def ejercicio2():
    while True:
        entrada = input("Introduce un número: ")
        try:
            num = float(entrada)
            break
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número.")
    
    if num > 0:
        print("El número es positivo.")
    elif num < 0:
        print("El número es negativo.")
    else:
        print("El número es 0.")

ejercicio2()
