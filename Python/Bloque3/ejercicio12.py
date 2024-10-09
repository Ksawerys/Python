def ejercicio12():
    ahorro_total = 0
    for mes in range(1, 13):
        ahorro_mensual = float(input(f"Introduce el ahorro del mes {mes}: "))
        ahorro_total += ahorro_mensual
        print(f"Ahorro acumulado hasta el mes {mes}: {ahorro_total}")

    print(f"Ahorro total en el año: {ahorro_total}")

ejercicio12()