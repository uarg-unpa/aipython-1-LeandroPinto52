nota = int(input("Ingrese nota"))
if nota <= 100 and nota >= 90:
    print("A")
elif nota < 90 and nota >= 70:
    print("B")
elif nota < 70 and nota >= 60:
    print("C")
elif nota < 60 and nota >= 50:
    print("D")
else:
    print("F")