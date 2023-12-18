import json
from pathlib import Path

# escribir json
products = [
    {"id": 1, "name": "Surfboard"},
    {"id": 2, "name": "Skate"},
    {"id": 2, "name": "Bicicleta"},
]

# data = json.dumps(products)
# Path("archivos/products.json").write_text(data)

# leer json
data = Path("archivos/products.json").read_text(encoding="utf-8")
prods = json.loads(data)

# Modificar json
prods[0]["name"] = "Chanchito feliz"
Path("archivos/products.json").write_text(json.dumps(prods))
