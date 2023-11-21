#6. Crear una función que calcule el factorial de un número.

def factorial(numero):
    #if numero == 1:
        #return numero
    #else:
        #return numero * factorial(numero - 1)
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

num = int(input("Ingrese numero: "))
print(factorial(num))
