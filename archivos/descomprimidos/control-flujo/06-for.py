for n in range(5):
    print(n, n * "Hola Mundo ")

# for else

buscar = 10

for n in range(5):
    if n == buscar:
        print("Encontrado: ", buscar)
        break
else:
    print("Número no encontrado")
