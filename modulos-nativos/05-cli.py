import os
from pathlib import Path
import sys


def cli(args):
    if len(args) == 1:
        print("No se pasaron argumentos")
    if len(args) != 3:
        print("Necesita dos argumentos")

    origin = args[1]
    o = Path(origin)
    if not o.exists():
        print("Origen no existe")
        return

    destiny = args[2]
    d = Path(destiny)
    if d.exists():
        print("EL destino no puede existir")
        return

    os.rename(str(origin), str(destiny))
    print("Archivo renombrado con exito")


cli(sys.argv)
