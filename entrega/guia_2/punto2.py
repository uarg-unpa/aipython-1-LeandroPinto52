#Compare su edad y mi edad usando if..else. ¿Quién es mayor (vos o yo)?,
#para el ingreso de la edad use input(“Ingrese su edad: ”)
#Use un condición anidada para:
    #Imprimir año si la diferencia es de 1, sino años para diferencias
    #mayores.
    #Cuando las edades son iguales imprimir un mensaje personalizado,
    #ser creativo!!

mi_edad = 19
su_edad = int(input("Ingrese su edad: "))

if su_edad > mi_edad and su_edad <= 20:
    print("Diferencia de 1 año")
elif su_edad > mi_edad and su_edad > 20:
    diferencia = su_edad - mi_edad
    print(f"Hay una diferencia de {diferencia} años")
elif su_edad == mi_edad:
    print("Nuestras edades son iguales!!1!1111!1!!1!!")
else:
    diferencia = mi_edad - su_edad
    print(f"Tiene {diferencia} años menos")