def ejercicio17():
    resultado = int(input("Introduce el resultado del dado (1-6): "))

    if resultado < 1 or resultado > 6:
        print("ERROR: número incorrecto.")
    else:
        opuesto = 7 - resultado
        numeros = ["uno", "dos", "tres", "cuatro", "cinco", "seis"]
        print(f"En la cara opuesta está el {numeros[opuesto - 1]}.")

ejercicio17()