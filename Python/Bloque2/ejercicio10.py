import math

def ejercicio10():
    x1 = float(input("Introduce x1: "))
    y1 = float(input("Introduce y1: "))
    r1 = float(input("Introduce r1: "))
    x2 = float(input("Introduce x2: "))
    y2 = float(input("Introduce y2: "))
    r2 = float(input("Introduce r2: "))
    
    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    if distancia > r1 + r2:
        print("Exteriores")
    elif distancia == r1 + r2:
        print("Tangentes exteriores")
    elif distancia < r1 + r2 and distancia > abs(r1 - r2):
        print("Secantes")
    elif distancia == abs(r1 - r2):
        print("Tangentes interiores")
    elif distancia < abs(r1 - r2):
        print("Interiores")
    elif distancia == 0 and r1 == r2:
        print("Concéntricas")

ejercicio10()