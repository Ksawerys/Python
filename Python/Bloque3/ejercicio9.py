def ejercicio9():
    base = float(input("Introduce la base: "))
    exponente = int(input("Introduce el exponente: "))
    resultado = 1

    for _ in range(exponente):
        resultado *= base

    print(f"{base} elevado a {exponente} es {resultado}")

ejercicio9()