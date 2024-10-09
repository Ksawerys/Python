def ejercicio14():
    tipo = input("Introduce el tipo de uva (A/B): ").upper()
    tamaño = int(input("Introduce el tamaño de la uva (1/2): "))
    precio_inicial = float(input("Introduce el precio inicial por kilo: "))
    kilos = float(input("Introduce los kilos de uva: "))

    if tipo == 'A':
        if tamaño == 1:
            precio_final = precio_inicial + 0.20
        elif tamaño == 2:
            precio_final = precio_inicial + 0.30
    elif tipo == 'B':
        if tamaño == 1:
            precio_final = precio_inicial - 0.30
        elif tamaño == 2:
            precio_final = precio_inicial - 0.50

    ganancia = precio_final * kilos
    print(f"La ganancia obtenida es: {ganancia} euros")

ejercicio14()