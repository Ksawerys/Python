def ejercicio5():
    while True:
        caracter = input("Introduce un carácter: ").lower()
        if caracter == ' ':
            break
        elif caracter in 'aeiou':
            print("VOCAL")
        else:
            print("NO VOCAL")

ejercicio5()