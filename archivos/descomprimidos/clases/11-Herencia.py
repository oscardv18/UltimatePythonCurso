class Animal:
    def comer(self):
        print("Comiendo")
    
class Perro(Animal):
    def pasear(self):
        print("Paseando")

class Chanchito(Perro):
    def programar(self):
        print("Programando")
    
perro = Perro()
perro.comer()
chanchito = Chanchito()
chanchito.comer()
chanchito.pasear()