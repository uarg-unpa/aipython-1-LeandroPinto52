#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual
#y el número de años, y muestre por pantalla el capital obtenido en la inversión.

cantidad_invertir = float(input("Ingrese cantidad a invertir"))
interes_anual = float(input("Ingrese interes anual"))
num_años = int(input("Ingrese numero de años"))

cantidad_por_año = (cantidad_invertir / interes_anual) * num_años
print(f"""Con la cantidad a invertir: {cantidad_invertir}, con el interes anual de:
{interes_anual} y con el numero de años: {num_años}, se obtiene: {cantidad_por_año}""")
