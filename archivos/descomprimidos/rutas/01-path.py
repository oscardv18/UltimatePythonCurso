from pathlib import Path

# Rutas en Windows
Path(r"C:\Archivos de Programas\Minecraft")
Path("/usr/bin")
Path()  # /home/username/project-directory
Path.home()
Path("one/__init__.py")


path = Path("hola-mundo/mi-archivo.py")
path.is_file()
path.is_dir()
path.exists()

print(path.name, path.stem, path.suffix, path.parent, path.absolute())

p = path.with_name("chanchito.py")
print(p)
p = path.with_suffix(".bat")
print(p)
