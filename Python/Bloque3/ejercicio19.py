def ejercicio19():
    while True:
        print("Menú:")
        print("1. Opción 1")
        print("2. Opción 2")
        print("3. Opción 3")
        print("4. Salir")
        opcion = int(input("Elige una opción: "))
        if opcion == 4:
            break
        elif opcion in [1, 2, 3]:
            print(f"Has elegido la opción {opcion}")
        else:
            print("Opción incorrecta")

ejercicio19()