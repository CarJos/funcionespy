'''13. Construir una función que reciba como parámetro un entero y un dígito y retorne la
cantidad de veces que se encuentra dicho dígito en dicho entero.
'''
def multiplo_digito(entero,digito):
    cont = 0
    if entero < 0:
        entero *= -1
    while entero != 0:
        ud = entero % 10
        if ud == digito:
            cont += 1
        entero = entero // 10
    return cont

def main():
    try:
        entero = int(input("Ingrese un numero entero: "))
        digito = int(input("Ingrese un digito: "))
        if digito < 10:
            compr = multiplo_digito(entero,digito)
            print("El digito se encuentra",compr,"veces en el entero")
        else:
            print("Debe ingresar solo un digito en el segundo valor")
    except ValueError:
        print("Error")

if __name__ == '__main__':
    main()