from abc import ABC, abstractmethod

class Model(ABC):
    @abstractmethod
    def save(self):
        pass

class User(Model):
    def save(self):
        print("Guardando en BBDD")
        
class Session(Model):
    def save(self):
        print("Guardando en archivo")

def save(entities):
    for entity in entities:
        entity.save()

user = User()
session = Session()

save([user, session])
