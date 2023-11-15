#4. Crear una lista de tus frutas favoritas

frutas = ["Manzana", "Banana", "Pera", "Sandia"]
print(frutas)

#a. Imprimir la longitud.
print("Longitud:", len(frutas))

#b. Eliminar el primer elemento de la lista.

del frutas[0]
print(frutas)

#c. Agregar un elemento al final de la lista.

frutas.append("Naranja")

#d. Imprimir los resultados anteriores.

print(frutas)

#5. Dada una lista mostrar el primer elemento, el del medio y el último.
print(frutas)
print(frutas[0])
mitad = int((len(frutas) - 1) / 2)
print(frutas[mitad])
print(frutas[len(frutas) - 1])
