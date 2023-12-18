from pathlib import Path

path = Path("rutas")
# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename("chanchito-feliz")

files = [p for p in path.iterdir() if not p.is_file()]
files = [p for p in path.glob("01-*.py")]
files = [p for p in path.glob("**/*.py")]
files = [p for p in path.glob("*.py")]
print(files)
