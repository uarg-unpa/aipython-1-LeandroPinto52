#8. Implementar una función que invierta un string.

    #hola
    #aloh

def invertirString(texto):
    textoInvertido = ""
    for i in range(len(texto) - 1, -1, -1):
        textoInvertido += texto[i]
    return textoInvertido

print(invertirString("Hola como estas"))

