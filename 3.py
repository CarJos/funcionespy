'''3. Construir una función que reciba como parámetro un entero y retorne la cantidad de
dígitos. 
'''
def cant_digitos():
    entero = int(input("Ingrese un numero entero: "))
    cont = 0
    if entero < 0:
        entero *= -1
    while entero != 0:
        cont += 1
        entero = entero // 10
    return cont

def main():
    try:
        cant = cant_digitos()
        if cant != 0:
            print("El numero tiene",cant,"digitos")
        else:
            print("El numero es un '0'")
    except ValueError:
        print("Error")

if __name__ == '__main__':
    main()