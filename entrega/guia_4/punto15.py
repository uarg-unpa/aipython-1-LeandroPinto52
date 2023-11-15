#15. Crear la siguiente lista:
flores = ["rosas", "orquídea", "lirio", "tulipan", "margarita", "dalia", "hortensia"]
print(flores)
#a. Mostrar tres elementos desde el tercer elemento.
for i in range(len(flores)):
    if i == 2:
        print(flores[i + 1 : len(flores) - 1])
        break

#b. Mostrar los elementos en posiciones pares desde la segunda posición

for i in range(len(flores)):
    if i > 1:
        if i % 2 == 0:
            print(f"['{flores[i]}']", end=" ")

#c. Mostrar todos los elementos desde la primera posición saltando de a tres
#elementos.
i = 0
while i < len(flores):
    print(flores[i])
    i += 3