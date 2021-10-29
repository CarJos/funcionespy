'''6. Construir una función que reciba como parámetro un entero y retorne el carácter al cual
pertenece ese entero como código ASCII.
'''
def a_caracter_ascii(entero):
    asci = chr(entero)
    return asci
def main():
    try:
        entero = int(input("Ingrese un numero entero: "))
        if entero > 0:
            cr_ascii = a_caracter_ascii(entero)
            print("El caracter que pertenece a",entero,"en codigo ascii es: ",cr_ascii)
        else:
            print("El numero debe ser positivo")
    except ValueError:
        print("Error")

if __name__ == '__main__':
    main()