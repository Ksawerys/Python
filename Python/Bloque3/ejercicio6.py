def ejercicio6():
    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))

    if num1 > num2:
        num1, num2 = num2, num1

    for i in range(num1, num2 + 1):
        if i % 2 == 0:
            print(i)

ejercicio6()