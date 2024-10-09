import random

def ejercicio2():
    numero_a_adivinar = random.randint(1, 100)
    intentos = 0
    max_intentos = 10

    while intentos < max_intentos:
        intento = int(input("Introduce un número: "))
        intentos += 1
        if intento < numero_a_adivinar:
            print("El número a adivinar es mayor")
        elif intento > numero_a_adivinar:
            print("El número a adivinar es menor")
        else:
            print(f"¡Has acertado en {intentos} intentos!")
            return

    print(f"Lo siento, has alcanzado el límite de intentos. El número era {numero_a_adivinar}")

ejercicio2()