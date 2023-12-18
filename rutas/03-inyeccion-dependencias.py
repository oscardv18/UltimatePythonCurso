from pathlib import Path

path = Path()
paths = [p for p in path.iterdir() if p.is_dir()]
print(paths)

dependencies = {
    "db": "conexion a la db",
    "api": "conexioon a la api",
    "graphql": "conexion a graphql",
}


def load(p):
    pkg = __import__(str(p).replace("/", "."))
    try:
        pkg.init(**dependencies)
    except:
        print("El paquete no tiene funciones")


list(map(load, paths))
# # Ejemplos de como realizar la inyeccion de dependencias
# class Perro:
#     def __init__(self, Correa):
#         self.correa = Correa()


# import Usuario


# def save():
#     user.save()


# def save(entity):
#     entity.save()


# def init_app(bbdd, api)
#     # inicializacion del modulo
