# Formas de Importar modulos y paquetes
# import usuarios.acciones # Forma tediosa
# from usuarios import acciones # Forma ideal 1
# from usuarios.impuestos.utilidades import save  # Forma ideal 2
from usuarios.impuestos.utilidades import pagar_impuestos  # Forma ideal 2
import usuarios

print(dir(usuarios))

# print(usuarios.gestion.__name__)
# print(usuarios.impuestos.__package__)
# print(usuarios.gestion.__path__)
# print(usuarios.impuestos.__file__)

print(__name__)
