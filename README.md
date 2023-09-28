# ULTIMATE PYTHON COURSE

## Python

Lenguahe de Programación Interpretado

### Herramientas incluidas en el paquete python3

- REPL (Read, Eval, Print, Lopp)

### Funcion para imprimir en consola

```python
print("Hello World")
```

Output: **Hello World**

### Tipos de Datos en Python

- String
- Integer
- Float
- Boolean **_(Los valores boolean empiezan con mayusculas, ej: True, False)_**

### Conversión de tipos

Se usan las siguientes funciones para poder convertir a sus respectivos tipos:

```python
    # int()
    # str()
    # float()
    # bool()
```

_Con Respecto a la función bool en python hay dos conceptos importantes: Truthy y Falsy esto quiere decir que habrán algunos datos que al pasar por esa función sean evaluados en true o false dependiendo del caso_

##### Los unicos datos que serán evaluados en false son

- Un string vacio ""
- El cero 0
- El tipo de dato None

## Control de Flujo

Las maneras de tener el control de flujo de nuestro código, python dispone de varias formas:

- _if_ para ejecutar el codigo que este dentro de su rango de indentación.

```python
edad = 55

if edad > 65:
    print("Puedes entrar con un super descuento!")
elif edad > 54:
    print("Puedes entrar con descuento!")
elif edad > 17:
    print("Puedes entrar")

print("Listo")

```

- Ciclo _for_ para recorrer algun tipo de dato que sea iterable

```python
for n in range(5):
    print(n, n * "Hola Mundo ")

# for else

buscar = 10

for n in range(5):
    if n == buscar:
        print("Encontrado: ", buscar)
        break
else:
    print("Número no encontrado")

```

- _if ternario_ es una forma mas corta de escribir el if

```python
edad = 15

message = "Es mayor" if edad > 18 else "Es Menor"

print(message)

```

- Ciclo _while_ es otro ciclo que posee python, este se ejecuta hasta que una determinada condicion sea False
_**NOTA: siempre agregar una forma de salir del ciclo cuando lo haga infinito, ya que estos consumen muchos recursos del computador**_

```python
numero = 1
while numero <= 100:
    print(numero)
    numero *= 2


# comand = ""
# while comand.lower() != "salir":
#     comand = input("$ ")
#     print(comand)

while True:
    command = input("$ ")
    print(command)
    if command.lower() == "salir":
        break
```

##### Comparaciones de Cadenas

Es una manera mas simple de escribir las condiciones:

```python
edad = 25

if 15 <= edad <= 65:
    print("Puedes entrar")
```

#### Operadores Logicos

- and
- or
- not

### Funciones

Es un bloque de codigo que se realiza una serie de tareas que se encuentran dentro de su rango de indentacion, pero no se ejecuta por si solo, requiere de una llamada para poder realizar sus labores.

```python
def hola(name, surname=""):
    print("Hello World")
    print(f"Bienvenido {name} {surname}")


hola("Oscar", "Diaz")
hola(surname="Diaz", name="Oscar")
```

#### Parametros de una funcion

Son las variables que se utilizan dentro de la misma y se encuentran en la definicion de ella.

#### Argumentos de una funcion

Son las variables que se le pasan a la funcion cuando esta es llamda.

#### xargs

Es una forma de hacer que una funcion tenga mas de un parametro sin necesidad de escribir una variable para cada uno:

```python
def sumar(*nums):
    result = 0
    for num in nums:
        result += num
    print(result)


sumar(1, 2)
sumar(1, 2, 3, 4, 5)
sumar(1, 2, 3, 4, 5, 12, 325)
```

#### kwargs

Es otra forma de tener multiples parametros dentro de una funcion, la diferencia es que estos seran ingresados dentro de un diccionario y para pasar los argumentos se deben de nombrar las variables:

```python
def get_products(**datos):
    print(datos["id"], datos["name"])


get_products(id="1312", name="iPhone",
             desc="Un nuevo tlf igual que el anterior pero mas caro")
```
