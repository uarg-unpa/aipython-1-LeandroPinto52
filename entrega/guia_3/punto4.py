num1 = int(input("Ingrese numero 1 "))
num2 = int(input("Ingrese numero 2 "))

if num1 > num2:
    for i in range(num2 + 1, num1):
        print(i)
else:
    for i in range(num1 + 1, num2):
        print(i)