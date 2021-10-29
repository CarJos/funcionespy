'''5. Construir una función que reciba como parámetro un entero y retorne la cantidad de
dígitos primos. 
'''
def cant_digito_primo():
    entero = int(input("Ingrese un numero entero: "))
    
    cont1 = 0
    ud = 0
    if entero < 0:
        entero *= -1
    while entero != 0:
        ud = entero % 10
        cont = 0
        for i in range(2,(ud//2)+1):
            if ud % i == 0:
                cont += 1
        if cont == 0 and ud != 1:
            cont1 += 1
        entero = entero // 10

    return cont1

def main():
    try:
        ctdpr = cant_digito_primo()
        if ctdpr != 0:
            print("El numero tiene",ctdpr,"digitos primos")
        else:
            print("El numero no posee digitos primos")
    except ValueError:
        print("Error")

if __name__ == '__main__':
    main()