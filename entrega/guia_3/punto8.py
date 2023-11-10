num = int(input("Ingrese numero mayor a 3 "))
while num <= 3:
    num = int(input("Ingrese numero mayor a 3 "))

for i in range(num):
    if i % 2 != 0:
        print(i)