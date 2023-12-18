import csv
import os

# Escribir archivos CSV
# with open("archivos/archivo.csv", "w") as file:
#     writer = csv.writer(file)
#     writer.writerow(["twit_id", "user_id", "text"])
#     writer.writerow(["1000", "1", "este es un twit"])
#     writer.writerow(["1001", "2", "este es otro twit!"])

# Leer un archivo CSV
# with open("archivos/archivo.csv") as file:
#     reader = csv.reader(file)
#     print(list(reader))
#     file.seek(0)
#     for line in reader:
#         print(line)

# Actualizar un CSV
with open("archivos/archivo.csv") as r, open("archivos/archivo_temp.csv", "w") as w:
    reader = csv.reader(r)
    writer = csv.writer(w)
    for line in reader:
        if line[0] == "1000":
            writer.writerow([1000, 1, "texto modificado"])
        else:
            writer.writerow(line)
    os.remove("archivos/archivo.csv")
    os.rename("archivos/archivo_temp.csv", "archivos/archivo.csv")
