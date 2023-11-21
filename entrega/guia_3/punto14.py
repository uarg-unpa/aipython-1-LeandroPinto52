num1 = int(input("Ingrese numero 1 "))
num2 = int(input("Ingrese numero 2 "))
if num1 > num2:
    for i in range(num2 + 1, num1):
        if i % 2 == 0:
            print(i)
elif num1 < num2:
    for i in range(num1 + 1, num2):
        if i % 2 == 0:
            print(i)
else:
    print("Son iguales")