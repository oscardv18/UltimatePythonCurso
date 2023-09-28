def reverse(text):
    t = text.lower()
    newText = ""
    for c in t:
        newText = c + newText
    return newText


def no_spaces(text):
    t = text.lower()
    newText = ""
    for c in t:
        if c != " ":
            newText += c
    return newText


def es_palindramo(texto):
    nospace = no_spaces(texto)
    newText = reverse(nospace)
    return texto.lower() == newText


result = es_palindramo("Abba")
print(result)
