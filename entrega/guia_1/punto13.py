#Escribir un programa que calcule el promedio de precios de 10 productos.

producto = []
suma = 0
for i in range(10):
    producto.append(int(input(f"Ingrese precio de producto {i + 1} ")))
    suma += producto[i]

promedio = suma / 10
print(f"El promedio de 10 productos es: {promedio}")