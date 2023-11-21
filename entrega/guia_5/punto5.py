#5. Implementar una función que determine si dado un número este es par o impar.

def esPar(numero):
    if numero % 2 == 0:
        print("Es par")
    else:
        print("No es par")

num = int(input("Ingrese numero: "))
esPar(num)