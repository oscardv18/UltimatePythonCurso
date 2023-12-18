n = 0
message = """
Bienvenidos a la Calculadora
Escribe 'salir' para Salir de la app
Las operaciones son: suma, resta, multi y div.
"""
print(message)

num = input("Ingrese número: ")

num = int(num)
while True:
    ope = input("Ingrese la Operación: ")
    if ope.lower() == 'suma':
        num2 = input("Ingrese el siguiente número: ")
        num2 = int(num2)
        num += num2
        print(f"El resultado es: {num}")
    elif ope.lower() == 'resta':
        num2 = input("Ingrese el siguiente número: ")
        num2 = int(num2)
        num -= num2
        print(f"El resultado es: {num}")
    elif ope.lower() == 'multi':
        num2 = input("Ingrese el siguiente número: ")
        num2 = int(num2)
        num *= num2
        print(f"El resultado es: {num}")
    elif ope.lower() == 'div':
        num2 = input("Ingrese el siguiente número: ")
        num2 = int(num2)
        num /= num2
        print(f"El resultado es: {num}")
    elif ope.lower() == "salir":
        break
