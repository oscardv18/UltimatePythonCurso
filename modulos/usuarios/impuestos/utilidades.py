if __name__ != "__main__":
    from ..gestion.crud import save  # import relativo

    # from usuarios.gestion.crud import save # import absoluto

    print(__name__)

    def pagar_impuestos():
        print("Pagando Impuestos")
        save()


if __name__ == "__main__":
    print("Tarea de Mantenimiento")
