def ejercicio18():
    dia = int(input("Introduce el día de la semana (1-7): "))
    dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]

    if 1 <= dia <= 7:
        print(f"El día correspondiente es {dias[dia - 1]}.")
    else:
        print("ERROR: número incorrecto.")

ejercicio18()