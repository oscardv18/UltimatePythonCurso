class Perro:
    patas = 4
    def __init__(self, name, age_old):
        self.name = name
        self.age_old = age_old

    def habla(self):
        print(f"{self.name} dice: Guau!")


Perro.patas = 3
mi_perro = Perro("Black", 1)
mi_perro.patas = 5
print(mi_perro.patas)
print(Perro.patas)
