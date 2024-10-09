import datetime

def ejercicio13():
    dia = int(input("Introduce el día: "))
    mes = int(input("Introduce el mes: "))
    año = int(input("Introduce el año: "))

    try:
        fecha = datetime.date(año, mes, dia)
        print("La fecha es correcta")
    except ValueError:
        print("La fecha es incorrecta")

ejercicio13()