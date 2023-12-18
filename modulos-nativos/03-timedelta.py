from datetime import datetime, timedelta

fecha1 = datetime(2023, 12, 23)
fecha2 = datetime(2024, 2, 14) + timedelta(weeks=1)

delta = fecha2 - fecha1

print(delta)
print("Dias Restantes:", delta.days)
print("Segundos Restantes:", delta.seconds)
print("Microsegundos Restantes:", delta.microseconds)
print("total_seconds()", delta.total_seconds())
