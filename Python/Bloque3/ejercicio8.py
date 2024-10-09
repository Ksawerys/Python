def ejercicio8():
    while True:
        limite_inferior = int(input("Introduce el límite inferior: "))
        limite_superior = int(input("Introduce el límite superior: "))
        if limite_inferior <= limite_superior:
            break
        print("El límite inferior debe ser menor o igual al límite superior. Inténtalo de nuevo.")

    suma = 0
    fuera_intervalo = 0
    igual_limite = False

    while True:
        numero = int(input("Introduce un número (0 para terminar): "))
        if numero == 0:
            break
        if limite_inferior <= numero <= limite_superior:
            suma += numero
        else:
            fuera_intervalo += 1
        if numero == limite_inferior or numero == limite_superior:
            igual_limite = True

    print(f"Suma de los números en el intervalo: {suma}")
    print(f"Números fuera del intervalo: {fuera_intervalo}")
    if igual_limite:
        print("Se ha introducido algún número igual a alguno de los límites del intervalo")

ejercicio8()