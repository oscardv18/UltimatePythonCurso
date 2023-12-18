users = [
    ["Oscar", 5],
    ["Pedrito", 1],
    ["Palotes", 4],
]

# Forma 1 / map
# nombres = []
# for user in users:
#     nombres.append(user[0])

print(users)

# Forma 2 / filter
nombres = [user[0] for user in users]
print(nombres)

ids = [user for user in users if user[1] > 2]
print(ids)

# Haciendo uso de map y filter
names = list(map(lambda user: user[0], users))
print(names)

names2 = list(filter(lambda user: user[1] > 2, users))
print(names2)