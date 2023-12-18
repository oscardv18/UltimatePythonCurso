from pathlib import Path
from zipfile import ZipFile

# escribir archivos comprimidos
# with ZipFile("archivos/comprimidos.zip", "w") as zip:
#     # Ruta actual: UltimatePythonCurso
#     for path in Path().rglob("*.*"):
#         print(path)
#         if str(path) != "archivos/comprimidos.zip":
#             zip.write(path)

# Leer un archivo comprimido
with ZipFile("archivos/comprimidos.zip") as zip:
    # print(zip.namelist())
    info = zip.getinfo("archivos/06-comprimidos.py")
    print(info.file_size, info.compress_size)
    zip.extractall("archivos/descomprimidos")
