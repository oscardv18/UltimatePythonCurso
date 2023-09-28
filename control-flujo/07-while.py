numero = 1
while numero <= 100:
    print(numero)
    numero *= 2


# comand = ""
# while comand.lower() != "salir":
#     comand = input("$ ")
#     print(comand)

while True:
    command = input("$ ")
    print(command)
    if command.lower() == "salir":
        break
