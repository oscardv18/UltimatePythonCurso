from io import open

# Escritura
text = "Hola Mundo!"
# file = open("archivos/hola-mundo.txt", "w")
# file.write(text)
# file.close()

# # Lectura
# file = open("archivos/hola-mundo.txt", "r")
# texto = file.read()
# file.close()
# print(texto)

# # Lectura como lista
# file = open("archivos/hola-mundo.txt", "r")
# texto = file.readlines()
# file.close()
# print(texto)

# with y seek
# with open("archivos/hola-mundo.txt", "r") as file:
#     print(file.readlines())
#     file.seek(0)
#     for line in file:
#         print(line)

# agregar
# file = open("archivos/hola-mundo.txt", "a+")
# file.write("Chao Mundo! :(")
# file.close()

# Lectura y Escritura
with open("archivos/hola-mundo.txt", "r+") as file:
    texto = file.readlines()
    file.seek(0)
    texto[0] = "Chanchito Feliz"
    file.writelines(texto)
