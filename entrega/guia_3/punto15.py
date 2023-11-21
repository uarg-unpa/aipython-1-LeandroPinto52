num = int(input("Ingrese numero "))
es_primo = True
if num > 1:
    i = 2
    while es_primo and i < num:
        if num % i == 0:
            es_primo = False
        i += 1

    if es_primo:
        print("El numero es primo")
    else:
        print("No es primo")
else:
    print("No es primo")