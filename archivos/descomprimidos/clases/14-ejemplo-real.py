class Model:
    table = False
    
    def __init__(self):
        if not self.table:
            print("Error, tienes que definir una table")
    
    def save(self):
        print(f"Guardando {self.table} en BBDD")
    
    @classmethod
    def search_by_id(cls, _id):
        print(f"Buscando por id {_id} en {cls.table}")

class User(Model):
    table = "users"

user = User()
user.save()
user.search_by_id(123)