# Aplicable con cuelquier iterable a excepcion de los diccionarios
lista = [1, 2, 3, 4]
print(1, 2, 3, 4)
print(*lista)

lista2 = [5, 6]
combinada = ["Hola", *lista, "Mundo", *lista2, "Chanchito"]
print(combinada)

# Caso para los diccionarios
punto1 = {"x": 19, "y": "hola"}
punto2 = {"y": 15}

nuevoPunto = {**punto1, "lala": "Hola Mundo", **punto2, "x": "Mundo"}
print(nuevoPunto)