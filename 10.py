'''10. Construir una función que reciba como parámetro un entero y retorne el primer dígito
de este entero. 
'''
def primer_digito():
    entero = int(input("Ingrese un numero entero: "))
    
    cont1 = 0
    ud = 0
    if entero < 0:
        entero *= -1
    if entero == 0:
        return 0
    while entero != 0:
        pd = entero
        entero = entero // 10
        

    return pd

def main():
    try:
        pdig = primer_digito()
        print("El primer digito del numero es: ",pdig)
    except ValueError:
        print("Error")

if __name__ == '__main__':
    main()