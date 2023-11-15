#12. Escribir una función que dada una lista de caracteres cuente la cantidad de vocales
#y retorne esa información.

def cantidadVocales(lista_caracteres):
    #contador = 0
    #for letra in lista_caracteres:
        #if letra in ('a', 'e', 'i', 'o', 'u'):
            #contador += 1
    #return contador
    return (lista_caracteres.count('a') + lista_caracteres.count('e') + lista_caracteres.count('i')
            + lista_caracteres.count('o') + lista_caracteres.count('u'))


caracteres = ['a', 'b', 'e', 'f', 'u', 'o']
print(cantidadVocales(caracteres))
