class Sistema:
    def __init__(self, usuario, contraseña):
        self.usuario = usuario
        self.contraseña = contraseña

    def verificar_acceso(self):
        usuarioInput = input("Introduce el nombre de usuario: ")
        contraseñaInput = input("Introduce la contraseña: ")
        if usuarioInput == self.usuario and contraseñaInput == self.contraseña:
            print("Has entrado al sistema.")
        else:
            print("Error: Usuario o contraseña incorrectos.")
    def funcionprueba(self):
        print("Hola")

class SistemaAvanzado(Sistema):
    def __init__(self, usuario, contraseña, nivel_acceso):
        super().__init__(usuario, contraseña)
        self.nivel_acceso = nivel_acceso

    def verificar_acceso(self):
        super().verificar_acceso()
        if self.nivel_acceso > 5:
            print("Acceso avanzado concedido.")
        else:
            print("Acceso básico concedido.")

# Ejemplo de uso
#sistema_basico = Sistema("pepe", "asdasd")
#sistema_basico.verificar_acceso()

sistema_avanzado = SistemaAvanzado("pepe", "asdasd", 7)
sistema_avanzado.funcionprueba()

cad= str(7.8)
"b" in cad
cadena = "ieyrg"
slice(cadena[::-8])
slice(cadena[2:3:-8])
slice(cadena[2:3])
cad ='''asdf'''
cad.endswith("asfd" , 0 ,10)
cad.startswith("asfd" , 0 ,10)
cad.strip(10)
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x**2, numeros))
print(cuadrados)  # Salida: [1, 4, 9, 16, 25]
list.
    #usuario = "pepe"
    #contraseña = "asdasd"
    
    #global usuario, contraseña
    #usuario = "pepe"
    #contraseña = "asdasd"