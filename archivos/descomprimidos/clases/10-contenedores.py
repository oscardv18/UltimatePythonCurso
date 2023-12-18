class Product:
    def __init__(self, name, price): 
        self.name = name
        self.price = price
    
    def __str__(self):
        return f"Producto: {self.name} - Precio: {self.price}"

class Category:
    products = []
    def __init__(self, name, productos):
        self.name = name
        self.products = productos
        
    def add_product(self, product):
        self.products.append(product)
    
    def print_Product(self):
        for product in self.products:
            print(product)

            
kayak = Product("Kayak", 600)
bicicleta = Product("Bicicleta", 300)
surfboard = Product("SurfBoard", 400)
deportes = Category("Deportes", [kayak, bicicleta])
deportes.add_product(surfboard)
deportes.print_Product()