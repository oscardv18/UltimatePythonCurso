lista = [32, 342, 12, 2, 23, 45]

lista.sort()
print(lista)

lista.sort(reverse=True)
print(lista)

lista2 = sorted(lista, reverse=True)
print(lista2)

users = [
    ["Oscar", 5],
    ["Pedrito", 1],
    ["Palotes", 4],
]


# def ordena(element):
#     return element[1]


# users.sort(key=ordena)
# print(users)

# ahora usando expresiones lambda:
users.sort(key=lambda el: el[1])
print(users)
