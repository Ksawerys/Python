def ejercicio20():
    peso = float(input("Introduce el peso del paquete en kg: "))
    zona = int(input("Introduce la zona de destino (1-5): "))

    if peso > 5:
        print("El paquete no puede ser transportado.")
        return

    coste_por_gramo = [24.00, 20.00, 21.00, 10.00, 18.00]
    if 1 <= zona <= 5:
        coste_total = peso * 1000 * coste_por_gramo[zona - 1]
        print(f"El coste total de la entrega es: {coste_total} euros")
    else:
        print("ERROR: zona incorrecta.")

ejercicio20()