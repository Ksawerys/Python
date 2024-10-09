# Escribir un programa que pida un nombre de usuario y una contraseña y si se ha introducido “pepe” y “asdasd” se indica “Has entrado al sistema”, sino se da un error
from ejercicio5Class import Sistema

sistema = Sistema("pepe", "asdasd")
sistema.verificar_acceso()