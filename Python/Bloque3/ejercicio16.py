def ejercicio16():
    N = int(input("Introduce el número de trabajadores: "))
    total_pagado = 0

    for trabajador in range(1, N + 1):
        horas = float(input(f"Introduce las horas trabajadas por el trabajador {trabajador}: "))
        sueldo = horas * 10  # Suponiendo que el sueldo por hora es 10 euros
        total_pagado += sueldo
        print(f"Sueldo del trabajador {trabajador}: {sueldo} euros")

    print(f"Total pagado por la empresa: {total_pagado} euros")

ejercicio16()