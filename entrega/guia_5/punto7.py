#7. Escribir una función que tome tres números como entrada y retorna el máximo.

def maximo(num1 : int, num2: int, num3: int) -> int:
    #return max(num1, num2, num3)
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    elif num3 >= num1 and num3 >= num2:
        return num3

print(maximo(5,9,2))