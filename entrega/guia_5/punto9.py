#9. Escriba una función que multiplique los elementos de una lista de números.

def mult_lista(lista):
    for i in range(len(lista)):
        lista[i] = lista[i] * 2
    return lista

numeros = [1,2,3,4]
print(mult_lista(numeros))