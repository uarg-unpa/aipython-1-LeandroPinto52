num = int(input("Ingrese un numero"))
cadena = ""
if num % 2 == 0:
    for i in range(0, num + 1, 2):
        print (i, cadena, sep=" ")
        cadena = str(i) + " " + cadena
else:
    for i in range(1, num + 1, 2):
        print(i, cadena, sep=" ")
        cadena = str(i) + " " + cadena
