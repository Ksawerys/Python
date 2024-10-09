def ejercicio11():
    A = float(input("Introduce el lado A: "))
    B = float(input("Introduce el lado B: "))
    C = float(input("Introduce el lado C: "))

    if A**2 + B**2 == C**2 or A**2 + C**2 == B**2 or B**2 + C**2 == A**2:
        print("Triángulo rectángulo")
    elif A == B == C:
        print("Triángulo equilátero")
    elif A == B or A == C or B == C:
        print("Triángulo isósceles")
    else:
        print("Triángulo escaleno")

ejercicio11()