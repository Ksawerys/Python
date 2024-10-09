def ejercicio15():
    pago_mensual = 10
    total_pagado = 0
    for mes in range(1, 21):
        total_pagado += pago_mensual
        print(f"Mes {mes}: {pago_mensual} euros")
        pago_mensual *= 2

    print(f"Total pagado después de 20 meses: {total_pagado} euros")

ejercicio15()