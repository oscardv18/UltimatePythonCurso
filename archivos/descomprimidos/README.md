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

#### Contenedores
Son clases a las que se les puede pasar en su contructor instancias de otras clases y dentro de esta se pueden realizar diferentes acciones con esta instancia.

#### Herencia
Es un concepto de OOP que se refiere a que una clase puede heredar metodos y propiedades de otra clase, la clase que hereda se le conoce como clase hija y la clase de la cuela hereda se le conoce como clase padre. En python para heredar de una clase simplemente despues del nombre de la clase se coloca dentro de parentesis el nombre de la clase padre `ClassName(FatherClass)`

#### Herencia Multiple
Es cuando una clase hereda metodo y propiedades de diferentes clases padres, estas clases padres son separadas por comas `ClassName(Class1, Class2, Class3...)`, hay que prevenir que los metodos de una clase sobreescriban los de otras, razon por la hay que tener cuidado con la arquitectura de nuestras clases.

#### Anulacion del Metodo
Tambien conocido como Override, se refiere a sobreescribir el comportamiento del metodo de una clase en otra, aqui tambien se incluyo, en esta parte del curso, la funcion `super()`, esta permite que se pueda acceder a los metodos y propiedades de la clase padre.

#### Clases Abstractas
Estas clases tienen la particularidad de que no se pueden instanciar, es decir, que se usan solamente para establecer una estructura y hacer que otras clases hereden de ella, la abstraccion permite que tengamos una idea conceptual de algo real y poder llevarlo a la practica sin necesidad de conocer a profundidad del tema.

En python para usar clases abstractas hay que importar ciertos modulos para que la clase que queramos que sea abstracta herede de ese modulo:

```python
from abc import ABC, abstractmethod

class Model(ABC):
    @property
    @abstractmethod
    def table(self):
        pass
    
    @abstractmethod
    def save(self):
        pass
    
    @classmethod
    def search_by_id(cls, _id):
        print(f"Buscando por id {_id} en {cls.table}")

class User(Model):
    table = "users"

    def save(self):
        print(f"Guardando {self.table} en BBDD")

user = User()
user.save()
user.search_by_id(123)
```

#### Polimorfismo
Permite que una clase tome diferentes formas, es decir, que varias clases pueden heredar de una clase padre en comun y heredan un mismo metodo en comun, pero, las clases hijas pueden tener una implementacion de la interfaz de manera diferente.

```python
from abc import ABC, abstractmethod

class Model(ABC):
    @abstractmethod
    def save(self):
        pass

class User(Model):
    def save(self):
        print("Guardando en BBDD")
        
class Session(Model):
    def save(self):
        print("Guardando en archivo")

def save(entities):
    for entity in entities:
        entity.save()

user = User()
session = Session()

save([user, session])
```

#### Extender Tipos nativos
Los tipos nativos de python se pueden extender para que tengan algunos metodos custom que nosostros mismo crearemos, por ejemplo, las listas pueden extenderse haciendo que una clase herede de `list` y luego se crean nuevas listas en base al contructor de la nueva clase que creamos para extender el tipo de dato:

```python
class Lista(list):
    def prepend(self, item):
        self.insert(0, item)

lista = Lista([1, 2, 3]) 
lista.append(4)
lista.prepend(0)

print(lista)
```

### EXCEPCIONES
Esta es una forma de poder controlar los errores en el codigo, probando una parte de el y si ocurre algun error lanzar una excepcion para indicar que fue lo que salio mal. Existen diferentes tipos de excepciones, las mas comunes son `ValueError`, `NameError`, para saber mas sobre los demas tipos es bueno consultar [este sitio](https://docs.python.org/es/3/library/exceptions.html)

Ademas de lanzar exepciones se pueden realizar otras acciones sea o no que ocurra un problema o que siempre se ejecute algo de codigo sin importar que resulte, estos son el `else:` y el `finally`. El `else` se ejecuta cuando no ocurrio ningun error y el `finally` siempre se ejecuta si importar el resultado

durante una parte de nuestro codigo podemos lanzar directamente algun tipo de excepcion, instanciandolo, y se le pasa a su contructor un mensaje que nosotros queramos que se ejecute y algun otro argumento. Por ejemplo la excepcion `ZeroDivisionError`:

```python
def div(n = 0):
    if n == 0:
        raise ZeroDivisionError("No se puede dividir entre 0", f"{n}")
    return 5 / n


try:
    div()
except ZeroDivisionError as e:
    print(e)

```

Para lanzar una excepcion directamente se utiliza la palabra reservada `raise`

Nos es muy recomendable tener mas de un par de excepciones ya que estas consumen muchisimos recursos. Pero no esta demas tener un par.

Nuestras excepciones pueden ser customizadas, simplemente hay que crear una clase hija que herede de la clase padre `Excepcion` y configurar el mensaje con el metodo magico `__str__`.


### Modulos
Un modulo es una porcion de nuestra aplicacion que se encuentra almacenada dentro de un archivo python  diferente al original, hay varias maneras de acceder a estos modulos desde cualquier archivo en el que queramos utilizarlos, en ese momento entran en juego las keywords `from` e `import`
```python
# Formas de Importar modulos y paquetes
import usuarios.acciones # Forma tediosa
from usuarios import acciones # Forma ideal 1
from usuarios.impuestos.utilidades import save  # Forma ideal 2
from usuarios.impuestos.utilidades import pagar_impuestos  # Forma ideal 2
```
Python, para hacer la carga de los modulos muchisimo mas rapida, se encarga de compilar estos y los guarda dentro de un directorio llamado `__pycache__` y si el modulo que estamos importando no ha tenido ningun cambio simplemente accedera a el por medio de este directorio, en el caso de que exista algun cambio simplemente se encargara de verificar la fecha de actualizacion del modulo con la del archivo compilado guardado en pycache y si la del modulo es una fecha mayor a la del compilado entonces volvera nuevamente a construir el archivo y lo guardara en pycache.

#### Paquetes
Los paquetes en python son los directorios en los que se encuentran diferentes modulos python, es decir, los modulos se refieren a los archivos con extension `.py` y los paquetes a los directorios en los que se organicen nuestras aplicaciones.

Pero, para que un direcorio sea reconocido como un paquete se debe crear dentro de el un archivo llamado: `__init__.py` dentro de el podemos realizar diferentes funciones para nuestro paquete y con solamente tener ese archivo dentro de un directorio ya el mismo es reconocido commo paquete.

Dentro de los paquetes pueden haber otros directorios y son llamados sub paquetes, de igual forma deben de tener todos el archivo `__init__.py`


#### Referenciando Sub-Paquetes
Para Referenciar a sub paquetes desde otros que esten en el mismo arbol de directorios del proyecto se hace uso de la navegacion de directorios como se hace en una shell unix, haciendo uno de los puntos dependiendo de donde se encuentre el paquete: `..paquete1.sub-paquete2.modulo`

#### dir()
Esta funcion que retorna una lista de todos los elementos (funciones magicas, modulos y sub-paquetes que tiene un directorio)

#### Paquetes con nombres dinamicos
Con el metodo magico `__name__` python nos devolvera el nombre del modulo desde el cual estamos ejecutando el script. Python es lo suficientemente inteligente para poder indicarnos si estamos ejecutando un archivo especifico de manera directa haciendo que el metodo magico devuelva un `__main__` esto ayuda para cuando tengamos que hacer labores de mantenimiento de nuestro codigo, pero solamente de un archivo especifico.

#### Condicionando imports
Podemos condicionar imports dependiendo desde donde estemos ejecutando nuestro codigo, por ejemplo si estamos ejecutando el codigo desde un archivo y queremos hacerle mantenimiento a dicho codigo simplemente verificamos si estamos ejecutando el script directamente con el punto anterior, en el caso de que no se ejecutado directamente condicionamos el codigo para que importe los modulos necesarios para trabajar cuando el archivo no se ejecute directamente:

```python
if __name__ != "__main__":
    from ..gestion.crud import save  # import relativo

    # from usuarios.gestion.crud import save # import absoluto

    print(__name__)

    def pagar_impuestos():
        print("Pagando Impuestos")
        save()


if __name__ == "__main__":
    print("Tarea de Mantenimiento")

```

### Rutas y Directorios

#### Rutas
En python para trabajar con Rutas y directorios se importa una clase llamada Path, que se encuentra desde el modulo libpath, esto permite que podamos referenciar una ruta, sin necesidad de que esta exista en nuestro equipos. Con ella podemos validarla, referenciarla, editarla, etc.

#### Directorios
Los directorios de trabajo se pueden referenciar mediante la siguiente sentencia: `path = Path("nombre del directorio")`

Al referenciar directorios, tenemos a la mano varios metodos, gracias a la clase Path, con la que podemos, por ejemplo, iterar el contenido de nuestro directorio y filtrar para que solo muestre los paquetes dentro del directorio o solo los modulos que terminan con la extension .py, entre otros.

#### Inyeccion de Dependencias
Nos permite reutilizar nuestro codigo, desacoplar el codigo para que se mucho mas facil de reutilizar, permite a escribir tests muchisimos mas faciles.

#### Import Dinamicos de paquetes
Para importar modulos y paquetes de manera dinamica se utiliza la funcion magica `__import__`.

Supongamos que tenemos dentro de nuestro proyecto dos directorios que son paquetes y dentro de estos hay un modulo cada uno y un archivo `__init__.py`, dentro de este archivo init hay una funcion con el mismo nombre `init()`, desde el archivo donde queremos importar dinamicamente estos modulos y paquetes simplemente se establece la ruta de path para nuestro proyecto actual: `path = Path()`, luego iteramos nuetro directorio para extraer de ahi una lista de solamente los directorios del proyecto, luego esos se les pasaran a una funcion que importara dinamicamente todos los paths para que posteriormente se ejecute el metodo init() que tienen los modulos principales de los paquetes.

```python
from pathlib import Path

path = Path()
paths = [p for p in path.iterdir() if p.is_dir()]
print(paths)

dependencies = {
    "db": "conexion a la db",
    "api": "conexioon a la api",
    "graphql": "conexion a graphql",
}


def load(p):
    pkg = __import__(str(p).replace("/", "."))
    try:
        pkg.init(**dependencies)
    except:
        print("El paquete no tiene funciones")


list(map(load, paths))
```

