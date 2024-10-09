def ejercicio16():
    duracion = int(input("Introduce la duración de la llamada en minutos: "))
    dia = input("Introduce el día de la semana: ").lower()
    turno = input("Introduce el turno (mañana/tarde): ").lower()

    if duracion <= 5:
        coste = duracion * 1
    elif duracion <= 8:
        coste = 5 * 1 + (duracion - 5) * 0.80
    elif duracion <= 10:
        coste = 5 * 1 + 3 * 0.80 + (duracion - 8) * 0.70
    else:
        coste = 5 * 1 + 3 * 0.80 + 2 * 0.70 + (duracion - 10) * 0.50

    if dia == "domingo":
        impuesto = 0.03
    elif turno == "mañana":
        impuesto = 0.15
    else:
        impuesto = 0.10

    coste_total = coste + (coste * impuesto)
    print(f"El coste total de la llamada es: {coste_total} euros")

ejercicio16()