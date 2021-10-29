'''4. Construir una función que reciba como parámetro un entero y retorne la cantidad de
dígitos pares. 
'''
def cant_digito_par():
    entero = int(input("Ingrese un numero entero: "))
    cont = 0
    ud = 0
    if entero < 0:
        entero *= -1
    while entero != 0:
        ud = entero % 10
        if ud % 2 == 0:
            cont += 1
        entero = entero // 10

    return cont

def main():
    try:
        ctdp = cant_digito_par()
        if ctdp != 0:
            print("El numero tiene",ctdp,"digitos pares")
        else:
            print("El numero no posee digitos pares")
    except ValueError:
        print("Error")

if __name__ == '__main__':
    main()