from pathlib import Path

archivo = Path("archivos/archivo-prueba.txt")
text = archivo.read_text("utf-8").split("\n")
text.insert(0, "Hola Mundo")
archivo.write_text("\n".join(text), "utf-8")
