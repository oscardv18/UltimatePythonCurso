class Perro:
    def __init__(self, name, age_old):
        self.__name = name
        self.age_old = age_old

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    def habla(self):
        print(f"{self.__name} dice: Guau!")
    
    @classmethod
    def factory(cls):
        return cls("Chanchito Feliz", 1)

perro1 = Perro.factory()
perro1.habla()
perro1.get_name()
print(perro1.__dict__)