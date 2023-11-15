#10. Crear una función que tome un string como parámetro y verifique si es un
#palíndromo. Ejemplo: Arenera, Narran. etc.

def palindromo(texto):
    texto = texto.lower()
    lista = []
    if len(texto) % 2 == 0:
        for letra in texto:
            if letra not in lista:
                lista.append(letra)
            elif letra in lista.pop():
                continue
            else:
                return False
    else:
        mitad = len(texto) / 2
        i = 0
        while i < mitad:
            lista.append(i)
            i += 1
        i += 1
        while i > len(texto):
            if i != lista.pop():
                return False
    return True
#No pensé una forma más facil de hacerlo sin una Pila

print(palindromo("Narran"))
