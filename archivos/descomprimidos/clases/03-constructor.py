class MiPerro:
    def __init__(self, name, age_old):
        self.name = name
        self.age_old = age_old

    def habla(self):
        print(f"{self.name} dice: Guau!")


mi_perro = MiPerro("Black", 1)
print(mi_perro.name)
print(mi_perro.age_old)
print(mi_perro.habla())
