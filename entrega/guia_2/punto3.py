#Solicite al usuario una contraseña, utilizando input(“Ingrese su contraseña”),
#almacene esta contraseña en una variable. Luego informar si la contraseña
#introducida coincide con la guardada sin tener en cuenta mayúsculas y
#minúsculas .

contraseña_guardada = "hoLA123456aSd"
contraseña = input("Ingrese su contraseña: ")

if contraseña.lower() == contraseña_guardada.lower():
    print("La contraseña coincide")
else:
    print("La contraseña no coincide")

