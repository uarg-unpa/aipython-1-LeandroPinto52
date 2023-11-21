#14. Implementar una función que tome una lista de números y retorna el promedio de
#sus elementos.

#def sumaLista(lista_numeros, indice):
    #if indice == 0:
        #return lista_numeros[indice]
    #else:
        #return lista_numeros[indice] + sumaLista(lista_numeros, indice - 1)

#def promedioLista(lista_numeros):
    #return sumaLista(lista_numeros, len(lista_numeros) - 1) / len(lista_numeros)

def promedioLista(lista_numeros):
    suma = 0
    for numero in lista_numeros:
        suma += numero
    promedio = suma / len(lista_numeros)
    return promedio

lista = [1,5,6,7,8]

print(promedioLista(lista))