edad = int(input("Ingrese edad"))
ingreso_mensual = int(input("Ingrese su sueldo"))

if edad < 18 or ingreso_mensual < 100000:
    print("No paga impuesto")
elif edad >= 18 and ingreso_mensual >= 100000:
    print("Debe pagar impuesto")
else:
    print("No paga impuesto")