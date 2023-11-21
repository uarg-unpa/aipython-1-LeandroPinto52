#4. Escribir una función que tome un número como entrada e imprima la tabla de
#multiplicar del 1 al 10, con el siguiente formato.
    #4 x 1 = 4

def tabla_multiplicacion(numero : int):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
    #return [numero * 1, numero * 2, numero * 3, numero * 4, numero * 5,
            #numero * 6, numero * 7, numero * 8, numero * 9, numero * 10]

num = int(input("Ingrese numero a multiplicar: "))
tabla_multiplicacion(num)