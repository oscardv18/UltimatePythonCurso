from abc import ABC, abstractmethod

class Model(ABC):
    @property
    @abstractmethod
    def table(self):
        pass
    
    @abstractmethod
    def save(self):
        pass
    
    @classmethod
    def search_by_id(cls, _id):
        print(f"Buscando por id {_id} en {cls.table}")

class User(Model):
    table = "users"

    def save(self):
        print(f"Guardando {self.table} en BBDD")

user = User()
user.save()
user.search_by_id(123)