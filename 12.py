''' 12. Construir una función que reciba como parámetro un entero y un dígito y retorne 1 si
dicho dígito está en dicho entero y 0 si no es así.
'''

def digito_en_entero(entero,digito):
    if entero < 0:
        entero *= -1
    while entero != 0:
        ud = entero % 10
        if ud == digito:
            return 1
            break
        entero = entero // 10
    if entero == 0:
        return 0

def main():
    try:
        entero = int(input("Ingrese un numero entero: "))
        digito = int(input("Ingrese un digito: "))
        if digito < 10:
            compr = digito_en_entero(entero, digito)
            print(compr)
        else:
            print("Debe ingresar solo un digito en el segundo valor")
    except ValueError:
        print("Error")

if __name__ == '__main__':
    main()