def ejercicio4():
    cantidad = int(input("Introduce la cantidad de números a introducir: "))
    mayores = 0
    menores = 0
    iguales = 0

    for _ in range(cantidad):
        numero = float(input("Introduce un número: "))
        if numero > 0:
            mayores += 1
        elif numero < 0:
            menores += 1
        else:
            iguales += 1

    print(f"Mayores que 0: {mayores}, Menores que 0: {menores}, Iguales a 0: {iguales}")

ejercicio4()

class Ejercicio4:
    def __init__(self, cantidad, mayores, menores, iguales):
        self.cantidad = cantidad
        self.mayores = mayores
        self.menores = menores
        self.iguales = iguales
     
    def verificar_acceso(self):
        print("Has entrado al sistema.")