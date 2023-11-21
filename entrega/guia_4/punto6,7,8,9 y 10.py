#6. Declarar una lista llamada datos_personales, insertar tu nombre, edad, altura,
#estado civil y dirección.

datos_personales = ["Leandro", 19, 1.72, "Soltero", "Joaquin Cabral"]


#7. Almacenar los nombres de tus compañías favoritas en una lista dándole esos datos
#como inicial.

compañias = ["Pepsi", "Nvidia", "Microsoft", "Motorola"]
print(compañias)

#8. Recorrer la lista del ejercicio 6 y mostrar los datos con print.

print(datos_personales)

#9. Recorrer la lista del ejercicio 7 y mostrar el índice más el nombre de la compañía.

for i in range(len(compañias)):
    print("Indice:", compañias.index(compañias[i]), "Compañia:", compañias[i])

#10. Modificar alguna/as de las compañía/s de la lista del ejercicio 7 y luego mostrar la
#lista.

compañias.insert(compañias.index("Microsoft"), "Sony")
compañias.remove("Microsoft")
print(compañias)
