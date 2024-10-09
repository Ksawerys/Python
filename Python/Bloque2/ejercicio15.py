def ejercicio15():
    alumnos = int(input("Introduce el número de alumnos: "))

    if alumnos >= 100:
        coste_por_alumno = 65
    elif 50 <= alumnos < 100:
        coste_por_alumno = 70
    elif 30 <= alumnos < 50:
        coste_por_alumno = 95
    else:
        coste_por_alumno = 4000 / alumnos

    pago_total = coste_por_alumno * alumnos
    print(f"El pago a la compañía de autobuses es: {pago_total} euros")
    print(f"Cada alumno/a debe pagar: {coste_por_alumno} euros")

ejercicio15()