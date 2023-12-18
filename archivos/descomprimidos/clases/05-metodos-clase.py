class Perro:
    patas = 4
    def __init__(self, name, age_old):
        self.name = name
        self.age_old = age_old

    @classmethod
    def habla(cls):
        print("Guau!")
    
    @classmethod
    def factory(cls):
        return cls("Chanchito Feliz", 1)

Perro.habla()
perro = Perro.factory()
print(perro.age_old, perro.name)
