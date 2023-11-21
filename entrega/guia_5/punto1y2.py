#1. Escribir una función que tome dos números y retorne la multiplicación entre ellos.

#def multiplicacion(num1, num2):
    #return num1 * num2

#print(multiplicacion(5,2))

#2. Modificar el ejercicio uno, en caso de que la invocación sea sin argumentos retorna
#siempre el producto de 1*1.

def multiplicacion(num1=1, num2=1):
    return num1 * num2

print(multiplicacion(5,2))
print(multiplicacion())
