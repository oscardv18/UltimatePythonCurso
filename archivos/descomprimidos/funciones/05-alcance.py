saludo = "Hello World"


def saludar():
    global saludo
    saludo = "Hola Mundo"


def saludaChanchito():
    saludo = 24
    print(saludo)


print(saludo)
saludar()
print(saludo)

# NUNCA USAR VARIABLES GLOBALES, se evita problemas con los tipos de datos o incoherencia de datos
