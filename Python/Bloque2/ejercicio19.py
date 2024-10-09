def ejercicio19():
    mes = int(input("Introduce un número de mes (1-12): "))
    dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if 1 <= mes <= 12:
        print(f"El mes tiene {dias_mes[mes - 1]} días.")
    else:
        print("ERROR: número incorrecto.")

ejercicio19()