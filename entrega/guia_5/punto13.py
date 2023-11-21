#13. Escribir una función que tome dos listas como parámetros y las intercale en una
#nueva, retornar la nueva lista resultante.

def nuevaLista(lista1, lista2):
    lista_nueva = []
    #while len(lista1) > 0 or len(lista2) > 0:
        #if len(lista1) > 0:
            #lista_nueva.append(lista1.pop())
        #if len(lista2) > 0:
            #lista_nueva.append(lista2.pop())
    #return lista_nueva
    i = 0
    while i < len(lista1) or i < len(lista2):
        if i < len(lista1):
            lista_nueva.append(lista1[i])
        if i < len(lista2):
            lista_nueva.append(lista2[i])
        i += 1
    return lista_nueva

lis1 = [5,8,3,4,5]
lis2 = ["hola", "como", "estas", " "]
lis3 = nuevaLista(lis1, lis2)
print(lis3)