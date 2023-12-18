n1 = input("Ingrese el Primer Número: ")
n2 = input("Ingrese el Segundo Número: ")

n1 = int(n1)
n2 = int(n2)

suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
div = n1 / n2

message = f"""
Para los número: {n1} y {n2}, estos son los siguientes resultados: 
Suma: {suma}
Resta: {resta}
Multiplicación: {multi}
División: {div}
"""
print(message)
