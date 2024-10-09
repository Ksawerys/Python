def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def ejercicio20():
    N = int(input("Introduce la cantidad de números primos a mostrar: "))
    contador = 0
    numero = 2
    while contador < N:
        if es_primo(numero):
            print(numero)
            contador += 1
        numero += 1

ejercicio20()