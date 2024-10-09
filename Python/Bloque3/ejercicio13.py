def ejercicio13():
    total_horas = 0
    for dia in range(1, 7):
        horas = float(input(f"Introduce las horas trabajadas el día {dia}: "))
        total_horas += horas

    sueldo = total_horas * 10  # Suponiendo que el sueldo por hora es 10 euros
    print(f"Total de horas trabajadas: {total_horas}")
    print(f"Sueldo total: {sueldo} euros")

ejercicio13()