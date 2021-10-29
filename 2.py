'''2. Construir una función que reciba como parámetro un entero y retorne sus dos últimos
dígitos.
'''
def ultimos_dos_digitos():
    entero = int(input("Ingrese un numero entero: "))
    if entero < 0:
        entero *= -1
    udd = entero % 100
    return udd

def main():
    try:
        udd = ultimos_dos_digitos()
        if udd > 9:
            print("Los ultimos dos digitos del numero son: ",udd)
        else:
            print("El numero no tiene dos digitos")

    except ValueError:
        print("Error")

if __name__ == '__main__':
    main()