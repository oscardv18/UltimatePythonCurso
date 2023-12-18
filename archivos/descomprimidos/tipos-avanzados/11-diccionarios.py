punto = { "x": 25, "y": 45}
print(punto)
print(punto["x"])
print(punto["y"])

punto["z"] = 75

if "lala" in punto:
    print("encontre lala: ", punto["lala"])

print(punto.get("x"))
print(punto.get("lala", 97))
del punto["x"]
del(punto["y"])

print(punto)
punto["x"] = 25

# formas de imprimir los datos de un diccionario
for valor in punto:
    print(valor, punto[valor])

print("Imprimir valor con .items")
for valor in punto.items():
    print(valor)

print("Imprimir valor y llave con .items")
for llave, valor in punto.items():
    print(llave, valor)

# caso de la vida real
users = [
    {"id": 1, "name": "Oscar"},
    {"id": 2, "name": "Camila"},
    {"id": 3, "name": "Chanchito"},
    {"id": 4, "name": "Feliz"}
]

for user in users:
    print(user["name"])