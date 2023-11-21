def comprobarExpresion(texto: str) -> bool:
    pila = []
    for simbolo in texto:
        if apertura(simbolo):
            pila.append(simbolo)
        else:
            if cierre(simbolo):
                if len(pila) > 0:
                    simbolo_apertura = pila.pop()
                    if not cierran(simbolo_apertura, simbolo):
                        return False
                else:
                    return False
    return len(pila) == 0
    
def cierran(carac1: str, carac2: str) -> bool:
    simbolos = {'{' : '}', 
                '[' : ']',
                '(' : ')'}
    return simbolos[carac1] == carac2

def apertura(carac: str) -> bool:
    return carac in ('{', '[', '(')

def cierre(carac: str) -> bool:
    return carac in ('}', ']', ')')

def main():
    while True:
        opcion = int(input("""Ingrese opcion:\n
        0 = Terminar programa\n
        1 = Ingresar texto para comprobar expresiones\n
        """))
        if opcion == 0:
            break
        elif opcion == 1:
            texto = input("Ingrese expresiones: ")
            if comprobarExpresion(texto):
                print("\nLa expresion es correcta\n")
            else:
                print("\nLa expresion no es correcta\n")
        else:
            print("\nNo es una opcion valida\n")
        continue

main()