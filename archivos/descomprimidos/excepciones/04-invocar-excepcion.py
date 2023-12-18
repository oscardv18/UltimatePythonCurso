def div(n = 0):
    if n == 0:
        raise ZeroDivisionError("No se puede dividir entre 0", f"{n}")
    return 5 / n


try:
    div()
except ZeroDivisionError as e:
    print(e)
