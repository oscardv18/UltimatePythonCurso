class Perro:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        print("Pasando por getter")
        return self.__name
    
    @name.setter
    def name(self, name):
        print("Pasando por setter")
        if name.strip():
            self.__name = name
        return
    
perro1 = Perro("Black")
print(perro1.name)