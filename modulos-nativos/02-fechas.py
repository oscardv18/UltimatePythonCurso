# import time

# print(time.time())

from datetime import datetime

fecha1 = datetime(2023, 12, 6, 10, 17, 36)
fecha2 = datetime(2023, 11, 30)

now = datetime.now()

fechaStr = datetime.strptime("31/01/22 23:59:59.999999", "%d/%m/%y %H:%M:%S.%f")
print(fechaStr)

print(fechaStr.strftime("%d.%m.%Y"))
print(fecha1 > fecha2)
print(
    fecha1.year,
    fecha1.month,
    fecha1.day,
    fecha1.hour,
    fecha1.minute,
    fecha1.second,
    fecha1.microsecond,
)
