try:
    n1 = int(input("Ingrese un numero: "))
except Exception as e:
    print("Ingrese un numero valido")
else:
    print("No ocurrio ningun error")
finally:
    print("Se ejecuta 100pre")