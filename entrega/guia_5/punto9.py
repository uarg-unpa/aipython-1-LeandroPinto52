#9. Escriba una función que multiplique los elementos de una lista de números.

def mult_lista(lista : list) -> int:
    resultado = 1
    for numero in lista:
        resultado *= numero
    return resultado

numeros = [1,2,3,4]
print(mult_lista(numeros))