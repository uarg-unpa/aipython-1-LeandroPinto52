#Cortar las dos primeras palabras de la frase ‘’El razonamiento matemático puede
#considerarse más bien esquemáticamente como el ejercicio de una combinación de
#dos instalaciones, que podemos llamar la intuición y el ingenio”.

texto = """El razonamiento matemático puede considerarse más bien esquemáticamente 
como el ejercicio de una combinación de dos instalaciones, que podemos llamar la intuición y el ingenio"""

texto = texto[27 : len(texto)]
print(texto)