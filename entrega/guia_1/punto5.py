#a Crear un programa que imprima un mensaje (usar función print) solicitando, el
#nombre, el apellido y la edad desde la terminal y luego darle un mensaje,“ser
#creativo”, utilizando los tres datos ingresados.

print("Ingrese su nombre")
nombre = input()
print("Ingrese su apellido")
apellido = input()
print("Ingrese su edad")
edad = input()

print(f"Hola {nombre} {apellido}, su edad es: {edad}")

#Modificar el ejercicio anterior para no utilizar la función print para mostrar el
#mensaje al solicitar los datos. Tip pasarle el argumento a la función input.

nombre = input("Ingrese su nombre ")
apellido = input("Ingrese su apellido ")
edad = input("Ingrese su edad ")

print(f"Hola {nombre} {apellido}, su edad es: {edad}")