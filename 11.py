'''11. Construir una función que reciba como parámetro un entero y un dígito y retorne 1 si
dicho entero es múltiplo de dicho dígito y 0 si no es así. 
'''

def multiplo_digito(entero,digito):
    if entero % digito == 0:
        return 1
    else:
        return 0

def main():
    try:
        entero = int(input("Ingrese un numero entero: "))
        digito = int(input("Ingrese un digito: "))
        if digito == 0:
            print("El digito debe ser mayor a 0")
        elif digito < 10:
            compr = multiplo_digito(entero,digito)
            print(compr)
        else:
            print("Debe ingresar solo un digito en el segundo valor")
    except ValueError:
        print("Error")

if __name__ == '__main__':
    main()