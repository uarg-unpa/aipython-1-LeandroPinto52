edad = int(input("Ingrese edad"))
if edad < 4:
    print("Entra gratis")
elif edad >= 4 and edad <= 18:
    print("Paga 5$")
else:
    print("Paga 10$")