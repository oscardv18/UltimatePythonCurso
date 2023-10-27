# EJERCICIO 1: Eliminar los espacios en blanco de un string y devolver una lista con los caracteres restantes.
TEXTO = "Hola Mundo este es mi stringeses"

def clear_white_spaces(txt):
    """function for clear white spaces in string

    Args:
        txt (string): text to clear

    Returns:
        string: text without white spaces
    """
    txt_clear = list(filter(lambda char: char != " ", txt))
    return txt_clear

newList = clear_white_spaces(TEXTO)
print(newList)

# EJERCICIO 2: Contar en un Diccionario cuanto se repiten los caracteres de un string 
def countCharString(txt):
    counter = {}
    for char in txt:
        if char != " ":
            counter[char] = txt.count(char)
    return counter

counterChars = countCharString(TEXTO)
print(counterChars)

# EJERCICIO 3: Ordenar las llaves de un diccionario por el valor que tienen y devolver una lista que contenga tuplas
def orderDictionary(dic):
    dic_items = list(dic.items())
    dic_items.sort(key=lambda el: el[1], reverse=True)
    return dic_items

dictio = orderDictionary(counterChars)
print(dictio)

# EJERCICIO 4: De un listado de tuplas, devolver las tuplas con el mayor valor.
def maxTuples(listOfTuples):
    tupleMax = listOfTuples[0][1]
    result = {}
    for orden in listOfTuples:
        if tupleMax > orden[1]:
            break
        result[orden[0]] = orden[1]
    return result

tuplMax = maxTuples(dictio)
print(tuplMax)

# EJERCICO 5 Crear un mensaje que diga, los caracteres que se repiten 4 veces son: 
# - A
# - B
def repeticiones(dic):
    message = "Los caracteres que mas se repiten son: \n"
    for key, value in dic.items():
       message += f"- {key.upper()} con {value} repeticiones \n" 
    return message

rept = repeticiones(tuplMax)
print(rept)