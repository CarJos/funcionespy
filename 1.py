'''1. Construir una función que reciba como parámetro un entero y retorne su último dígito. 
'''
def ultimo_digito():
    entero = int(input("Ingrese un numero entero: "))
    if entero < 0:
        entero *= -1
    ud = entero % 10
    return ud

def main():
    try:
        ud = ultimo_digito()
        print("El ultimo digito del numero es :",ud)
    except ValueError:
        print("Error")

if __name__ == '__main__':
    main()