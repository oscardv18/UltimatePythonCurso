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

### Tipos Avanzados
Estos son los tipos de datos adicionales que posee python, entre ellos:

- **Listas**, es un tipo de dato iterable que puede contener valores de cualquier otro tipo e incluso puede tener listas anidadas.

#### Formas de Manipular las listas:
Haciendo uso de los corchetes y si lo que se necesita es extraer cierta parte de la lista usando los dos puntos '[:]'

Para crear listas tambien se puede hacer uso de la funcion `list()` que viene incluida en python.

_**Dato curioso, para hacer una lista con numero que vayan del 1 al 10 se le puede pasar de argumento la funcion `range(11)` a la funcion `list(range(11))`**_

Las listas tambien se pueden desempaquetar, esto se realiza mediante la asignacion de varias variables a una sola lista, entonces, se le ira asignando cada valor en el orden de izquierda a derecha a cada variable:
```python
nums2 = list(range(1, 11))
primero, segundo, *otros, pen_u, ultimo = nums2
print(nums2)
print(primero, segundo, otros, pen_u, ultimo)
```

En el caso de que se coloque una variable de la forma: `*otros` quiere decir que tomara todos los valores, en el caso de que despues de esa variable con esa notacion se asigna el ultimo elemento de la lista, aunque depende mucho de la cantidad de variables que esten despues.

#### Iterar Listas:
Las listas son tipos iterables, y se pueden recorrer por medio de los ciclos, como el `for`, pero cuando se iteran no se puede acceder a su indice, para eso se debe de pasar la lista como argumento a la funcion `enumerate(nombre_lista)` y esa funcion nos devolvera el indice y el valor.

```python
mascotas = ["Pelusa", "Lusin", "Yuni", "Catira", "Gambeta"]

for indice, mascota in enumerate(mascotas):
    print(indice, mascota)
```

#### Buscar Elementos en Listas
La funcion `nombre_lista.count()` devuelve el indice del valor que se le pase de argumento, si este no se encuentra dentro devuelve un error, para verificar si existe o no se puede colocar esa funcion dentro de una condicion que verifique la existencia dentro de la lista del elemenerror, para verificar si existe o no se puede colocar esa funcion dentro de una condicion que verifique la existencia dentro de la lista del elemento.

#### Agregar o eliminar elementos

- _Para agregar elementos_, se utilizan los metodos `lista.insert(elemento)` y la funcion `lista.append(elemento)`, estos insertan elementos en la lista original al inicio y al final de dicha lista respectivamente.

- _Para eliminar elementos_, se utilizan las funciones `lista.remove(elemento)`, `lista.pop()` este tiene la particularidad de eliminar el ultimo elemento de la lista; existe tambien una forma de eliminar elementos: `del lista[indice]` y se puede eliminar todos los valores de la lista usando: `lista.clear()`, eso vacia completamente la lista.

#### Ordenar Listas
Para ordenar de manera ascendente una lista se usa la funcion  `lista.sort()`, de manera descendente: `lista.sort(reverse=True)`.

Hay casos en los que puede haber una lista con listas dentro de ella (listas anidadas) y se quiera ordenar por un identificador que posea esa lista dentro, simplemente se hace uso de las funciones anonimas o en python se conocen como lambda, simplemente se le pasa como argumento a la funcion `lista.sort(lambada_funcion)`, la funcion lambda devolvera el valor del elemento por el cual se quiere que se ordene la funcion.

```python
users.sort(key=lambda el: el[1])
print(users)
```

#### Comprension de Listas
Permiten extraer o transformar nuestras listas en otras con informacion de relevancia. Haciendo uso de un `for` abreviado dentro de una lista podemos extraer el dato especifico que se necesite, en el tambien podemos condicionar que datos traer, es decir, filtrarlos.

Python incluye dos metodos que hacen esas mismas acciones respectivamente, la funcion `map` y `filter` la diferencia es que estos se usaran como argumentos de la funcion `list(map())` `list(filter())`. `map` y `filter` reciben una funcion lambda como argumento.

#### Tuplas
Es exactamente los MISMO que una lista, la unica diferencia es que no se pueden modificar de ninguna forma, se puede crear tuplas a partir de una lista usando el metodo `tuple([valores])`

#### Sets
Significa grupo o conjunto, es una coleccion de datos en la que los datos no se pueden repetir y no estan ordeandos, hay dos formas de crear un set, la primera es declarandolo con llaves `{}` y la segunda forma es con la funcion `set(lista[])`.

Los sets tienen cuatro operadores fundamentales para trabajar con ellos:

- **Union `|`**: une dos sets eliminando los valores repetidos.

- **Interseccion `&`**: Devuelve un set con los valores que se encuentren en los sets que se esten operacionalizando con el operador de interseccion.

- **Diferencia `-`**: este se encarga de eliminar los elementos del primer set que a su vez se encuentran en el segundo.

- **Diferencia Simetrica `^`**: este operador se encarga de devolver un nuevo set que tendra los elementos que no se encuentren presente en ambos sets

#### Diccionarios:
Es una coleccion de datos de tipo `key:value`, donde la `key` se colocal dentro de comillas y por medio de ella es que se va a obtener el valor, si es que se usa la forma en la que se obtienen valores de las listas `nombre_diccionario["keyname"]`, python incluye una funcion para los diccionarios llamada `diccionario.get("key")`, que es una manera mas 'limpia' de obtener los valores, para eliminar una llave y valor de un diccionario se usa el prefijo `del` o la funcion `del()` incluida dentro de python, para recorrer un diccionario se usa el metodo `diccionario.items()` que devuelve una lista con las llaves y los valores del diccionario, tambien se puede desempaquetar esto.

#### Operador de Desempaquetado
Este operador se encarga de desempaquetar automaticamento cualquier iterable, para todos los iterables menos los diccionarios se usa el `*` para desempaquetar y en el caso de los diccionarios se usa el `**`.

#### Filas
Estas cumplen la caracteristicas de FIFO (First in, First out), siguienlo el ejemplo de una fila en el mundo real (filas en el supermercado, pagos, etc). Pero al seguir esa convencion, la logica nos dice que cuando en una lista se elimina el primer elemento segun el comportamiento de una fila debemos correr un espacio hacia atras los elementos de la misma, pero eso ocuparia mucho espacio de computo, simplemente usamos el modulo de python que se importa desde `collections`, llamado: `deque`

`deque(lista)`, se encarga de crear la fila y asi usar solamente los metodos que son necesarios para emular el comportamiento de una fila real, para agregar elementos se usa `fila.append(element)`, para eliminar un elemento siempre sera el primero de la fila se usa `file.popleft()`

#### Pilas
Su caracteristica es LIFO (Last in, First out). Ejemplo de esto: Un Historial de Navegacion. Para asegurarnos de trabajar con su comportamiento y estructura, se declara una lista comun en python, pero solo se hace uso de los metodos `lista.append()` y el metodo `lista.pop()`, para cumplir con la caracteristica LIFO.

### CLASES

#### Constructor
Las clases con el plano de construccion de un objeto, el constructor de una clase en python se escribe de la siguiente manera: `def __init__()`

#### Parametro self
Todos los metodos de una clase deben llevar el parametro `self` que hacer referencia a la clase en la que se encuentra, se podria decir que es el reemplazo de `this` en otros lenguajes de programacion

#### Propiedades privadas
Para escribir propiedades se debe anteponer al identificador de la propiedad doble guion bajo: `__propiedad`, para acceder a ella se implementan los getters y setters 

#### Metodos de Clases
Es un decorador `@classmethod` que permite que los metodos de una  clases se puedan usar sin necesidad de instanciar una clase, por ejemplo, se puede crear un metodo llamado `factory()` que devuelva la instancia de la clase automaticamente

```python
@classmethod
    def factory(cls):
        return cls("Chanchito Feliz", 1)

perro = Perro.factory()
```
A los metodos de clases en lugar del parametro `self` se coloca el parametro `cls` que este hace referencia a la clase a la cual pertenece el metodo

#### Decorador property
Este decorador se encarga de convertir un metodo en una propiedad y a su vez permite que otro metodo que se use para settear esa propiedad en especifico se convierta en el setter del metodo al que se le aplica el decorador property:

```python
class Perro:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        print("Pasando por getter")
        return self.__name
    
    @name.setter
    def name(self, name):
        print("Pasando por setter")
        if name.strip():
            self.__name = name
        return
    
perro1 = Perro("Black")
print(perro1.name)
```
El metodo que se quiera usar como setter se le aplica un decorador con el nombre del metodo convertido en propiedad seguido de un punto y la palabra: 'setter': `@name.setter`

#### Metodos Magicos
Estos metodos vienen incluidos para todas las clases que creemos en python, cada uno realiza una accion diferente o similar para las clases. Para informarse mas de los metodos magicos se puede consultar [este sitio](https://rszalski.github.io/magicmethods/#:~:text=What%20are%20magic%20methods%3F,__%20or%20__lt__%20).

```python
class Perro:
    def __init__(self, name, age_old):
        self.name = name
        self.age_old = age_old
    
    def __del__(self):
        print(f"Chao Perro☹️: {self.name}")

    def __str__(self):
        return f"Clase Perro: {self.name}"

    def habla(self):
        print(f"{self.name} dice: Guau!")

perro = Perro("Black", 12)
print(perro)
del perro
```

En el caso del metodo `__str__` este se usa para customizar la forma en la que se muestra informacion de nuestra clase; el metodo magico `__del__` se utiliza cuando se va a destruir una instancia de una clase. **Todos los metodos magicos empiezan con dobles guiones bajos y terminan con dobles guiones bajos**.

#### Comparacion de Objetos
La comparacion de objetos se basa en comparar si algunos de los datos que le estamos pasando a dos instancias diferentes son iguales o no, mayores o menores que otro, mayores-igual o menor-igual que otra instancia. Esto se realiza por medio de algunos metodos magicos: `__eq__`, `__ne__`, `__lt__`, `__le__`, cada uno corresponde a: igual, no igual, menor que, menor-igual que. Python es lo suficientemente intuitivo como para entender que se ya esta la logica de condicion para que dos instancias sean iguales sabra cuando no lo seran, esto da como resultado de que no sea necesario escribir la logica de 'no igual', mismo caso con el 'menor que' y el 'menor-igual que', ya python sabe cuando aplicara la logica de sus contrapartes.
