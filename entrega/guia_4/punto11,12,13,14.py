#11. Crear una lista de números del 1 al 10.
numeros = []
for i in range(1, 11):
    numeros.append(i)

#a. Imprimir los tres primeros números utilizando rebanadas.
print(numeros[0 : 3])

#12. Crear una lista de letras (‘a’ hasta ‘j’)

letras = ['a','b','c','d','e','f','g','h','i','j']

#a. Imprima cada segundo elemento usando rebanadas.
print(letras)
i = 1
while i < len(letras):
    print(letras[i : i + 1], end=" ")
    i += 2

#13. Crear una lista a su criterio.

numeros_dos = [1,2,3,4,5,6,7,8,9,10,11,12,13]

#a. Imprimir la lista en forma inversa usando rebanadas.
print()
i = -1
maximo = 0 - len(numeros_dos)
while i >= maximo:
    print(numeros_dos[i : i + 1], end=" ")
    i -= 1
print()
#No encontré una forma para mostrar todos en inverso con rebanadas

#14. Crear una lista de tus palabras favoritas

palabras = ["Computadora", "Musica", "Argentina", "Juegos", "Libertad", "Arte"]
print(palabras)

#a. Extraer una sub lista conteniendo desde la segunda hasta la cuarta palabra.

palabras_sub = palabras[1 : 4]
print(palabras_sub)