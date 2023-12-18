class Perro:
    def __init__(self, name, age_old):
        self.name = name
        self.age_old = age_old
    
    def __del__(self):
        print(f"Chao Perro☹️: {self.name}")

    def __str__(self):
        return f"Clase Perro: {self.name}"

    def habla(self):
        print(f"{self.name} dice: Guau!")

perro = Perro("Black", 12)
print(perro)
del perro