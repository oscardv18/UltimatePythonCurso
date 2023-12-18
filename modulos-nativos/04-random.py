import random
import string

lista = list(range(1, 11))
random.shuffle(lista)
print(
    random.random(),
    random.randint(1, 10),
    lista,
    random.choice(lista),
    random.choices(lista, k=3),
    "".join(random.choices("asdfqewr", k=3)),
)

chars = string.ascii_letters
digits = string.digits
selection = random.choices(chars + digits, k=16)

password = "".join(selection)
print(password)
