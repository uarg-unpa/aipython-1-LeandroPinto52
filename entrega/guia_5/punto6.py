#6. Crear una función que calcule el factorial de un número.

def factorial(numero):
    if numero == 1:
        return numero
    else:
        return numero * factorial(numero - 1)

num = int(input("Ingrese numero: "))
print(factorial(num))
