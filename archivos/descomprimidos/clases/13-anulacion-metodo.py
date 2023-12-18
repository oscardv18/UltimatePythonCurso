class Ave:
    def __init__(self):
        self.volador = "volador"
    
    def vuela(self):
        print("Vuela Ave")
        
class Pato(Ave):
    def __init__(self):
        super().__init__()
        self.nada = "Nadador"
    
    def vuela(self):
        super().vuela()
        print("Vuela pato")

pato = Pato()
pato.vuela()
print(pato.volador)
print(pato.nada)
