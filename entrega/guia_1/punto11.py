#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el
#costo por hora. Después debe mostrar por pantalla el sueldo que le corresponde.

num_horas = int(input("Ingrese la cantidad de horas trabajadas "))
costo_horas = float(input("Ingrese el costo por hora "))
sueldo = costo_horas * num_horas
print(f"El sueldo que le corresponde es de: {sueldo}")

