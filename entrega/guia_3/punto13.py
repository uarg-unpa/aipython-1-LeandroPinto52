#13.Construir un programa que lea un número natural N y calcule la suma de los
#primeros N números pares.

num = int(input("Ingrese numero"))
suma = 0
if num > 1:
    for i in range(1, num + 1):
        if i % 2 == 0:
            suma += i
    print(suma)
else:
    print(num)
